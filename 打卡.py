# coding=utf-8
import requests
import random
import json

headers =  {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',}

login_url = 'https://www.shanbay.com/accounts/login'

news_list_url = 'http://www.shanbay.com/api/v1/read/news/?page=1'

finish_url = 'https://www.shanbay.com/api/v1/read/article/user/{}/'

checkin_url = "http://www.shanbay.com/api/v1/checkin/?for_web=true"

def login(username, password):
    #创建Session对象，该对象会自动保存cookie信息
    s = requests.Session()
    # 首先获得登录表单的csrftoken，这个在提交用户账号和密码的时候要一起提交
    csrftoken = s.get(login_url).cookies['csrftoken']
    login_form_data = {'username': username,
                       'password': password,
                       'csrfmiddlewaretoken': csrftoken
                 }
    # s，即session里保存了cookie信息，下面的post之后，s中会添加更多认证信息，包括auth_token，之后用s访问其他页面
    res = s.post(login_url, data=login_form_data, headers=headers)
    return s

def get_unfinished_news(s, num):
    # 每天要阅读一定数量的新闻后才能打卡，这里就是要获得首页中尚未阅读过的新闻，num指今天要完成的新闻阅读篇数
    # 通过保存了cookie信息的Session对象s访问news_list_url可以获得首页的新闻列表
    news_list = s.get(news_list_url)
    # 获得的数据是json格式的，所有的news信息都在data这个key里，为了便于处理，将其转化为python的dict对象
    news_list = json.loads(news_list.text)['data']
    news_id_list = []
    for news in news_list:
        # 先保存其中没有阅读过的news，同时保存min_used_seconds字段，稍后可根据该字段的值估计每篇文章的阅读时间，这个值是news单词数的两倍
        if news['is_finished'] is False:
            # 设置一下我们完成一篇news的阅读所需要的时间，这里我简单做了两倍的处理
            my_used_seconds = news['min_used_seconds']*2
            news_id_list.append((news['id'], my_used_seconds))
    # 首页中未阅读过的news大概有10篇，我们没必要读完10篇，这里根据设定的num值获得前num篇，当然num>2
    return news_id_list[:num]
def shanbay_auto_checkin(username, password, num, int):
    # form_data 为提交的完成阅读信息
    s = login(username, password)
    unfinished_news = get_unfinished_news(s, num)
    if not unfinished_news:
        print('Checkin Failed! The news of first_page already were finished...')
        return
    for news_id, my_used_seconds in unfinished_news:
        # 通过浏览器的抓包工具观察，扇贝对于每篇新闻是按照分页后每一页分别post数据的，
        # 前面的分页都有三个字段，只有最有一个分页有如下两个字段，经测试，我们可以直接post最后页的数据
        finished_form_data = {'operation': 'finish',
                              'used_time': my_used_seconds}
        # 注意这里用的是put方法，至于用哪种http方法，可以通过浏览器的抓包工具查看每次请求的method和要提交的表单数据
        read_res = s.put(finish_url.format(news_id), data=finished_form_data)
        # 根据返回的状态码，判断完成阅读信息是否成功put
           if read_res.json()['status_code'] == 0:
                print('Finished_news_id:{};Used_seconds:{}'.format(news_id, my_used_seconds))
           else:
                print('news_id:{};reading failed!'.format(news_id))
       except KeyError:
            print(read_res)
            print('Please check your username or password!')
    checkin_res = s.post(checkin_url, headers=headers)
    # 这里判断是否打卡成功，一天只能打卡一次，如果已打卡一次，第二次执行该脚本时虽然完成阅读，但不能打卡
    if checkin_res.json()['status_code'] == 0:
        print('Checkin successfully')
    else:
        print('Checkin Failed! Maybe you already have a checkin...')
if __name__ == '__main__':
    username = '你的用户名'
    password = '密码'
    num = random.randint(5, 7) #这里设置每天随机阅读3-6篇
    shanbay_auto_checkin(username, password, num)
