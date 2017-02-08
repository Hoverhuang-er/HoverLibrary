#coding=utf8
import os
import requests
import itchat, time
from itchat.content import *
from NetEaseMusicApi import interact_select_song


KEY = '51127407c5884fafbf00a33cf53078f4'

def get_respone(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'   : KEY,
        'info'  : msg,
        'userid': 'wechat-robot'
    }
    try:
        r = request.post(apiUrl,data=data).json()
        return r.get('text')
    except:
        return
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I recived' + msg['Text']
    reply = get_respone(msg['Text'])
    return reply or defaultReply


@itchat.msg_register([ MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def download_files(msg):
    with open(msg['FileName'], 'wb') as f:
        f.write(msg['Text']())

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('您好!', msg['RecommendInfo']['UserName'])

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])

itchat.auto_login(True)
itchat.send(HELP_MSG,'filehelper')
itchat.run()
