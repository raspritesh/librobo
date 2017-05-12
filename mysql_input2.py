import MySQLdb as msdb
import rfidreader1
import time
db=msdb.connect("localhost","root","ritesh","library")
import RPi.GPIO as gpio

sql="""CREATE TABLE IF NOT EXISTS rfids(id varchar(10) primary key)"""
pin=5
cur=db.cursor()
gpio.setmode(gpio.BOARD)
gpio.setup(pin,gpio.OUT)
cur.execute(sql)
res=0

while True:
        gpio.output(pin,gpio.LOW)
	res=rfidreader1.reading()
	print res
	sql="select id from rfids where id='%s' ;"%res
	cur.execute(sql)
	if cur.fetchone() is not None:
                gpio.output(pin,gpio.HIGH)
                print "Already exist"
		u=1;
		
		
	elif res!=None:
		sql=" insert into rfids(id) values('%s');"%res
		try:
                        gpio.output(pin, gpio.LOW)
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
