from flask import Flask, json, jsonify , request ,url_for
from threading import Thread
import process as proc
from threading import Thread
import socket
from threading import Thread
import mysql.connector as db
import os
import logging as log
import logging as lgapi
import gc

gc.enable()


#log.basicConfig(filename='/dataset/'+hostname+'tratamento.log', encoding='utf-8', level=log.DEBUG)
#lgapi.basicConfig(filename='/dataset/'+hostname+'apilog.log', encoding='utf-8', level=lgapi.DEBUG)


receb = True

db_user = str( os.environ['db_user'] )
db_pass = str( os.environ['db_pass'] )
db_address = str( os.environ['db_address'] )
dbase = str( os.environ['db'] )


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
log.debug(local_ip)
paths = os.environ['dataset']

print("HOSTNAME")
print(hostname) 

cursor  = db.connect( host= db_address , user= db_user , password= db_pass , database=dbase )
cur = cursor.cursor()
" select * from "
cur.execute("insert into proc (proc, hostname) select 1, '"+hostname+"' from dual where not exists (select proc, hostname from proc where hostname = '"+hostname+"');")
cursor.commit()
cursor.close()

###########################################
log.basicConfig(filename='/dataset/'+hostname+'tratamento.log', encoding='utf-8', level=log.DEBUG)
lgapi.basicConfig(filename='/dataset/'+hostname+'apilog.log', encoding='utf-8', level=lgapi.DEBUG)
###########################################

class Process(Thread):
    def __init__ (self, file):
        Thread.__init__(self)
        self.file = file

    def run(self):
        log.debug ("Start Process")
        ret = proc.tratamento(self.file)
        proc.writeF(paths+''+self.file+'done', str(ret.summary()) )
        log.debug("conectando")
        cursor  = db.connect( host= db_address , user= db_user , password= db_pass , database=dbase )
        log.debug("conectou")
        cur = cursor.cursor()
        cur.execute("update arquivo set tii = now(), verif = 2 where arquivo ='"+self.file+"'")
        cursor.commit()

        cur.execute("update proc set proc = 1  WHERE hostname='"+hostname+"'")
        cursor.commit()

        cursor.close()
        log.debug ("End Process")
        gc.collect()
        global receb
        receb = True





app = Flask(__name__)
@app.route("/analise",methods=["POST"])
def analise():
    gc.collect()
    global receb
    post_var_ = json.loads(request.data)
    file = post_var_.get("fileName",0)
    #################################################################################################
    lgapi.debug("ARQUIVO RECEPCIONADO"+file)
    lgapi.debug("BANCO : CONECTANDO EM BANCO DE DADOS")
    cursor  = db.connect( host= db_address , user= db_user , password= db_pass , database=dbase )
    lgapi.debug("BANCO : CONECTADO EM BANCO DE DADOS")
    cur = cursor.cursor()
    log.debug(receb)

    cur.execute(" select proc from proc  WHERE hostname='"+hostname+"'  ");
    rsi = cur.fetchall()
    for x in rsi:
        passa = x[0]

    cursor.commit();
    if passa == 1:
        cur.execute(" update proc set proc = 0  WHERE hostname='"+hostname+"' ")
        cursor.commit()

        cur.execute("update arquivo set tif = now(), verif = 1, hostname = '"+hostname+"'  where arquivo ='"+file+"'")
        lgapi.debug("ATUALIZANDO ARQUIVO EM BANCO")
        #global receb
        #receb = False
        a = Process(file)
        a.start()
    else:
        lgapi.debug("**** Ja temos um arquivo sendo analisado ****")


    cursor.commit()
    cursor.close()
    return "Arquivo estara sendo analisado"


if __name__ == "__main__":
    debug = True
    app.run(host=local_ip, port=7777, debug=debug)

