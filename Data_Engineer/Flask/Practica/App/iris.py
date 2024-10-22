from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from pathlib import Path
import traceback
import pickle
import os

def entrenar_modelo_cls():
    '''Función para entrenar modelo de clasificación con KNN'''
    try:
        iris = load_iris()

        X = pd.DataFrame(iris['data'], columns=iris['feature_names'])
        y = iris['target']
        # print(X)
        # print(y)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 42)

        # print(X_train)
        # print(y_train)

        knn = KNeighborsClassifier(n_neighbors=5)
        knn.fit(X_train, y_train)

        predicc = knn.predict(X_test)

        print(accuracy_score(y_test,predicc))
        return knn
    except Exception as a:
        traceback.print_exc()
        print(f"No se pudo terminar el proceso por {a}")

def guardar_modelo(model):
    '''Función para guardar en un pkl el modelo entrenado y poder cargarlo'''
    try:
        ruta = Path(os.getcwd(), 'Data_Engineer', 'Flask', 'Practica', 'App', 'knn_model.pkl')
        with open(ruta, 'wb') as archivo:
            pickle.dump(model, archivo)
    except Exception as a:
        traceback.print_exc()
        print(f"No se pudo terminar el proceso por {a}")

if __name__ == '__main__':
    modelo = entrenar_modelo_cls()
    print(os.getcwd())
    guardar_modelo(modelo)

print('Modelo entrenado')


