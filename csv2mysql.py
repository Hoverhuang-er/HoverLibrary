import csv
import pymysql

#mysql db connection
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='ENTER DATABASE NAME HERE')
cur = conn.cursor()

with open('.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	i=0
	for row in reader:
		query = "insert into TABLENAME (column1, column2, column3) VALUES ('"+row['id']+"', '"+row['age']+"', '"+row['fav_no']+"', '"+row['something_else']+"')"
		cur.execute(query)
		i+=1
		if(i%1000==0):
		  #commit after every 1000 queries executed
			conn.commit()
			print(i)
		#final commit
	conn.commit()
cur.close()
conn.close()
print("Done")