import MySQLdb as msdb
import rfidreader1
import time
db=msdb.connect("localhost","root","ritesh","library")

sql="""CREATE TABLE IF NOT EXISTS rfids(id varchar(10) primary key)"""

cur=db.cursor()

cur.execute(sql)
res=0
while True:
	res=rfidreader1.reading()
	
	print res
	sql="select id from rfids where id='%s' ;"%res
	cur.execute(sql)
	if cur.fetchone() is not None:
		print "Already exist"
		u=1;
	elif res!=None:
		sql=" insert into rfids(id) values('%s');"%res
		try:
			cur.execute(sql)
			db.commit()
		except:
			print "*"
			u=0;
			db.rollback()
	else:
		break

	time.sleep(3)
	
	
db.close()
