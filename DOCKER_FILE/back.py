import numpy as np
from flask import Flask, json, jsonify , request ,url_for
from threading import Thread
#from giroscopio import 


app = Flask(__name__)

#@app.route("/getVelocidade")
#def getVelocidade():
#    return (f"Tudo Funcionando Corretamente {Valores} !", 200) 

vM1 = 0   
vM2 = 0  
vM3 = 0   
vM4 = 0    
@app.route("/sendSingnalSpeed",methods=["POST"])
def sendSingnalSpeed():
    velocidade_ = json.loads(request.data)
    vM1 = velocidade_.get("vM1",0)
    vM2 = velocidade_.get("vM2",0)
    vM3 = velocidade_.get("vM3",0)
    vM4 = velocidade_.get("vM4",0)
    
    return (f"\n HOST 1 \n {vM1} \n {vM2} \n {vM3} \n {vM4}", 200)

if __name__ == "__main__":
    debug = True # com essa opção como True, ao salvar, o "site" recarrega automaticamente.
    app.run(host='0.0.0.0', port=5000, debug=debug)