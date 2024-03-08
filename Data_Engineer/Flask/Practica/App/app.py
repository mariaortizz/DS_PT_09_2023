from flask import Flask, request
import pickle
from pathlib import Path
import os

ruta_modelo = Path(os.getcwd(), 'Data_Engineer', 'Flask', 'Practica', 'App', 'knn_model.pkl')
model = pickle.load(open(ruta_modelo, 'rb'))

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return '<h1>APP FLASK IRIS</h1>'

@app.route('/predict', methods = ['POST'])
def predict(a,b,c,d):
    a = float(request.args.get('a', None))
    b = float(request.args.get('b', None))
    c = float(request.args.get('c', None))
    d = float(request.args.get('d', None))
    prediccion = model.predict([[a,b,c,d]])
    return 'la predicción es {}'.format(prediccion)

if __name__ == '__main__':
    app.run(debug=True)