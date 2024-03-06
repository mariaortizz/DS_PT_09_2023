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
