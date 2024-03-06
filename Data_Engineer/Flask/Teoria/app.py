<<<<<<< HEAD
from flask import Flask


#IMPORTA EL ARCHIVO DE CONFIGURACIÓN
app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")
# app.config.from_pyfile("config.py")

app = Flask(__name__)
print(app) #nombre del archivo

@app.route('/')
def index(): #se declara la url de raiz
    print(app.config[BCRYPT_LOG_ROUNDS])
    return "<h1>Hola Maria</h1>"

@app.route('/maria')
def index_1(): #se declara la url de raiz
    return "<h1>Hola Maria_segundo paso</h1>"

@app.route("/user/<name>") #esto es para que sea dinamica
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)

if __name__ == '__main__':
    app.run(debug=True) 
    #debg true es lo que hace que puedas llevar los cambios directo a la pagina, 
    #sino que volver a pedir la pagina. Solo lo dejamos cuando estamos en prueba


from flask import Flask, jsonify
import numpy as np
from datetime import datetime

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")
# app.config.from_pyfile("Data_Engineer/Flask/Teoria/config.py")

@app.route('/')
def index():
    print('esto no funciona en la web pero si en la terminal')
    print(app.config['BCRYPT_LOG_ROUNDS'])
    return "<h1>Hola Solecito!</h1>"

@app.route('/rodrigo')
def index1():
    return "<h1>Rodrigo estuvo aquí!</h1>"

print('esto no funciona')

@app.route(f"/user/{app.config['BCRYPT_LOG_ROUNDS']}/<name>")
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)

@app.route("/user/<name>/<int:ind>")
def index2(name, ind):
    mylist = ['2024/03/06', 'elemento2', False, 'elemento4']
    mydict = {'key': -ind}
    mytuple = (datetime.now().date().strftime('%Y/%m/%d'), None, 'tuple3', np.nan)
    return jsonify(name=name, myindex=ind, mylist=mylist, mydict=mydict, mytuple=mytuple)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=8910)


