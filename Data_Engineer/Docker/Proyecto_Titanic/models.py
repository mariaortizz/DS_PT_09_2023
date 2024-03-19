import pickle
import zipfile
import traceback
import inspect
import numpy as np
import pandas as pd


def extraccion_modelo(ruta_modelo):
    '''Función para extraer el modelo que tenemos y cargarlo en un zip'''
    try:
        with open(ruta_modelo, 'rb') as archivo:
            model = pickle.load(archivo)
        return model 
    except Exception as a:
        traceback.print_exc()
        func = inspect.stack()[1].function
        print(f"No se pudo terminar el proceso en la función {func} por {a}")

def extraccion_escalado(ruta_escaler):
    '''Función para extraer el cluster que tenemos en pickle'''
    try:
        with open(ruta_escaler, 'rb') as archivo:
            km = pickle.load(archivo)
        return km 
    except Exception as a:
        traceback.print_exc()
        func = inspect.stack()[1].function
        print(f"No se pudo terminar el proceso en la función {func} por {a}")

def aplicar_escalado(nuevo_dato1, nuevo_dato2, escaler):
    '''Funcion para escalar los datos que entran nuevos'''
    try:
        nuevos_datos = np.array([nuevo_dato1, nuevo_dato2]).reshape(1, -1)
        datos_e = escaler.transform(nuevos_datos)
        return datos_e[0][0], datos_e[0][1]
    except Exception as a:
        traceback.print_exc()
        func = inspect.stack()[1].function
        print(f"No se pudo terminar el proceso en la función {func} por {a}")

def transf_sex(x):
    '''Función para transformar los datos que recibimos'''
    try:
        valores_sex = {
            "female": 0,
            "male": 0,
        }

        valores_sex[x] = 1

        Sex_female = valores_sex['female']
        Sex_male = valores_sex['male']

        return Sex_female, Sex_male
    except Exception as a:
        traceback.print_exc()
        func = inspect.stack()[1].function
        print(f"No se pudo terminar el proceso en la función {func} por {a}")

def transf_embarked(x):
    '''Función para transformar los datos que recibimos'''
    try:
        valores_embarked = {
            "C": 0,
            "Q": 0,
            "S": 0,
        }

        valores_embarked[x] = 1

        Embarked_C = valores_embarked['C']
        Embarked_Q = valores_embarked['Q']
        Embarked_S = valores_embarked['S']

        return Embarked_C, Embarked_Q, Embarked_S
    except Exception as a:
        traceback.print_exc()
        func = inspect.stack()[1].function
        print(f"No se pudo terminar el proceso en la función {func} por {a}")

def aplicar_modelo(model, Pclass, SibSp, Parch,
                                    Age_e, Fare_e, Sex_female, Sex_male, Embarked_C,
                                    Embarked_Q, Embarked_S):
    '''Función para aplicar el cluster a los datos nuevos que tenemos'''
    try:

        data = {'Pclass' : [Pclass],
                            'SibSp' : [SibSp], 
                            'Parch' : [Parch], 
                            'Age' : [Age_e],
                            'Fare' : [Fare_e], 
                            'Sex_female' : [Sex_female], 
                            'Sex_male' : [Sex_male],
                            'Embarked_C' : [Embarked_C],
                            'Embarked_Q' : [Embarked_Q],
                            'Embarked_S' : [Embarked_S]
        }
        valores = pd.DataFrame(data)
        prediccion = model.predict(valores)
        print(prediccion)
        return prediccion
    except Exception as a:
        traceback.print_exc()
        func = inspect.stack()[1].function
        print(f"No se pudo terminar el proceso en la función {func} por {a}")

