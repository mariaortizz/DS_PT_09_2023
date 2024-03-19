'''Archivo por el que corre la aplicación'''
from flask import Flask, render_template, request
import os 
from pathlib import Path
from models import extraccion_escalado, transf_embarked ,\
    extraccion_modelo, aplicar_escalado, transf_sex, aplicar_modelo

ruta_modelo = Path(os.getcwd(), 'src', 'model', 'modelo_rf.pkl')
ruta_escalado = Path(os.getcwd(), 'src', 'model', 'standar_scaler.pkl')

MODELO = extraccion_modelo(ruta_modelo)
ESCALER = extraccion_escalado(ruta_escalado)

# os.chdir(os.path.dirname(__file__))

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")

@app.route('/', methods = ['GET'])
def home():
    return render_template("home.html")

@app.route('/formulario')
def formulario():
    return render_template("formulario.html")


@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    try:

        if request.method == 'POST':

            Pclass = float(request.form['Pclass'])
            SibSp = float(request.form['SibSp'])
            Parch = int(request.form['Parch'])
            Age = int(request.form['Age'])
            Fare = float(request.form['Fare'])
            Sex = request.form['Sex']
            Embarked = request.form['Embarked']

            Sex_female, Sex_male= transf_sex(Sex)
            Embarked_C, Embarked_Q, Embarked_S = transf_embarked(Embarked)

            Age_e, Fare_e = aplicar_escalado(Age, Fare, ESCALER)

            predd = aplicar_modelo(MODELO, Pclass, SibSp, Parch,
                                    Age_e, Fare_e, Sex_female, Sex_male, Embarked_C,
                                    Embarked_Q, Embarked_S)

            dicc = {0 : 'Muerto', 1 : 'Sobrevivido'}

            return render_template("predict.html", prediccion = dicc[predd[0]])
        else:
            return "Metodo no permitido"
    except ValueError:
        return render_template("error.html")

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=5001)