from flask import Flask, json, jsonify , request ,url_for
from threading import Thread
import process as proc
from threading import Thread
import socket
from threading import Thread
import mysql.connector as db
import os 

receb = True

db_user = str( os.environ['db_user'] )
db_pass = str( os.environ['db_pass'] )
db_address = str( os.environ['db_addres'] )
dbase = str( os.environ['db'] )


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(local_ip)
paths = os.environ['dataset']
class Process(Thread):
    def __init__ (self, file):
        Thread.__init__(self)
        self.file = file

    def run(self):
        print ("Start Process")
        ret = proc.tratamento(self.file)
        proc.writeF(paths+''+self.file+'done', str(ret.summary()) ) 
        print("conectando")
        cursor  = db.connect( host= db_address , user= db_user , password= db_pass , database=dbase )
        print("conectou")
        cur = cursor.cursor()
        cur.execute("update arquivo set tii = now(), verif = 2 where arquivo ='"+self.file+"'")
        cursor.commit()
        cursor.close()
        print ("End Process")
        global receb 
        receb = True 





app = Flask(__name__)
@app.route("/analise",methods=["POST"])
def analise():
    global receb
    post_var_ = json.loads(request.data)
    file = post_var_.get("fileName",0)
    #################################################################################################
    print("conectando")
    cursor  = db.connect( host= db_address , user= db_user , password= db_pass , database=dbase )
    print("conectou")
    cur = cursor.cursor()
    print(receb)
    if receb == True:
        cur.execute("update arquivo set tif = now(), verif = 1, hostname = '"+hostname+"'  where arquivo ='"+file+"'")
        print("update") 
        #global receb 
        receb = False
        a = Process(file)
        a.start()
    else:
        print("Já temos um arquivo sendo analisado") 
    cursor.commit()
    cursor.close()
    return "Arquivo estara sendo analisado"


if __name__ == "__main__":
    debug = True # com essa opção como True, ao salvar, o "site" recarrega automaticamente.
    app.run(host=local_ip, port=7777, debug=debug)
