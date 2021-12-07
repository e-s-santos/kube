import time 
import mysql.connector as db
import os

db_user = str( os.environ['db_user'] )  
db_pass =  str(  os.environ['db_pass'] )
db_address =  str(  os.environ['db_address'] )
db_name =  str( os.environ['db_name']  )

print(db_user)
print(db_pass)
print(db_address) 
print(db_name) 

a = open('/tmp/query','r')
for i in a.readlines():
        print("Conectando") 
        for x in i.split(";"):
            print("----") 
            cursor  = db.connect(host= db_address, user= db_user, password= db_pass, database=db_name)
            print("conectou")
            cur = cursor.cursor()
            print(x) 
            cur.execute(x)
            cursor.commit()
            cursor.close()
        time.sleep(5)

ar = open('/tmp/query','w')
ar.write("")
ar.close()
