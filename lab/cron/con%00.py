import mysql.connector as db 
print("importado")
from subprocess import call
import os 
import time as t

#while True:
db_user = str( os.environ['db_user'] ) 
db_pass = str( os.environ['db_pass'] ) 
db_address = str( os.environ['db_addres'] ) 
dbase = str( os.environ['db'] )
#wstime = int( os.environ['wstime'] )
print("User") 
print(db_user)
print("Pass")
print(db_pass)
print("Address")
print(db_address)
print("db")
print(dbase)
#print("Segundos") 
#print(wstime) 
for val in range(1):
    try:
        #cursor  = db.connect(host='10.96.22.85', user='root', password='passwordRoot', database='mimosa')
        cursor  = db.connect(host= db_address , user = db_user, password = db_pass, database = dbase)
        cur = cursor.cursor()
        cur.execute("select arquivo from arquivo where verif = 0")
        rs = cur.fetchall()
        arq = ""
        print("Antes do for")
        for i in rs:
            print("dentro do for") 
            t.sleep(10) 
            print(i)
            arq = i[0]
        #cursor.commit()
            #cur.execute("update arquivo set verif = 1 where arquivo = '"+arq+"'") 
            os.system("curl --location --request POST 'http://192.168.1.14:30008/analise' --header 'Content-Type: application/json'  --data-raw '{\"fileName\": \""+arq+ "\"}'")
        cursor.commit()
        #print( )
        #call("curl --location --request POST 'http://192.168.1.14:30008/analise' --header 'Content-Type: application/json'  --data-raw '{\"fileName\": \" "+arq+ " \"}'", shell=True)
    except db.Error as error:
	    if error.errno == errorcode.ER_BAD_DB_ERROR:
		    print("Database doesn't exist")
	    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		    print("User name or password is wrong")
	    else:
		    print(error)
    else:
	    cursor.close()
