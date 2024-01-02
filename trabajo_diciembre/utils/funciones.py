import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.stats import kurtosis, skew, probplot, shapiro, spearmanr, kruskal
from geopy.geocoders import Nominatim
import time
import pandas as pd
import plotly.express as px
import re
import traceback

def cardinalidad(data):
    '''Funcion para saber la cardinalidad de las varibales que tenemos en el data frame'''
    try:
        df_cardin = pd.DataFrame([{
                    'variable' : i,
                    'tipo_dato' : data[i].dtypes,
                    'cantidad_de_nulos' : data[i].isna().sum(),
                    'valores_unicos' : data[i].unique(),
                    'cardinalidad' : data[i].nunique(),
                    'porcentaje_cardinalidad' : (data[i].nunique()/data.shape[0])*100
                } for i in data])
        
        df_tipo_variable = pd.DataFrame({'tipo_variable' : ['nominal', 'continua', 'discreta', 'nominal', 
                                                            'nominal', 'ordinal', 'ordinal',
                                                            'nominal', 'ordinal', 'ordinal', 'nominal']}) #TODO
        
        df_cardinalidad = pd.concat([df_cardin,df_tipo_variable], axis = 1)
    except Exception as a:
        traceback.print_exc()
        print(f"No se pudo procesar el DataFrame por  {a}")

    return df_cardinalidad

def graficos_variables_cuant(data):
    ''''Función para graficar las variables cuantitativas'''
    media_color = 'r'
    mediana_color = 'b'
    try:
        for columna in data.columns:
            print('--'*30)
            print(f"VARIABLE: {columna}\n")

            media = data[columna].mean()
            mediana = data[columna].median()

            plt.figure(figsize=(20,4))
            sns.boxplot(data[columna], orient='h')
            plt.axvline(media, color = media_color, linestyle = 'dashed', linewidth = 1)
            plt.axvline(mediana, color = mediana_color, linestyle = 'dashed', linewidth = 1)

            plt.show()

            sns.displot(data[columna], rug = True, bins = 30)
            plt.axvline(media, color = media_color, linestyle = 'dashed', linewidth = 1, label = f'Media: {media:.0f}')
            plt.axvline(mediana, color = mediana_color, linestyle = 'dashed', linewidth = 1, label = f'Mediana: {mediana:.0f}')

            plt.title(f'Distribución de {columna}')
            plt.legend()

            plt.show()

            print(data[columna].describe().round())
            print('--'*30)
    except Exception as a:
        print(f"No puedo analizar la variable por este error {a}")

def graficos_variables_cualit(data):
    ''''Función para graficar las variables cualitativas'''
    try:
        for columna in data.columns:
            print('--'*50)
            print(f"VARIABLE: {columna}\n")
            if len(data[columna].dropna().unique()) < 30:
                ax = sns.countplot(data= data, y= columna)
                # ax.set_xticklabels(data[columna].sort_values().unique(), rotation=90)
                plt.title(f"Conteo variable {columna}")
                plt.show();
            else:
                print('Son demasiados valores únicos no se puede graficar')
            print(data[columna].describe(include= 'all'))
            print('--'*50)
    except Exception as a:
        traceback.print_exc()
        print(f"No puedo analizar la variable por este error {a}")

def graficos_box_plot(data):
    ''''Función para graficar las variables mediante grafico tipo Boxplot'''
    media_color = 'r'
    mediana_color = 'b'
    try:
        for columna in data.columns:
            print('--'*30)
            print(f"VARIABLE: {columna}\n")

            plt.figure(figsize=(20,4))
            sns.boxplot(data[columna], orient='h')

            try:
                media = data[columna].mean()
                mediana = data[columna].median()
                
                plt.axvline(media, color = media_color, linestyle = 'dashed', linewidth = 1)
                plt.axvline(mediana, color = mediana_color, linestyle = 'dashed', linewidth = 1)
                print(data[columna].describe().round())
            except:
                pass

            plt.show()

            
            print('--'*30)
    except Exception as a:
        traceback.print_exc()
        print(f"No puedo analizar la variable por este error {a}")


def cambiar_precio_a_euros(data):
    ''' Función para cambiar el precio de los dispositivos a euros
    Input : DataFrame
    Output : DataFrame'''

    try:
        data['precio_euros'] = data['price'].apply(lambda x: ((float(re.sub(r'[^\d.]', '', x))*0.011)/1))
        data.drop(columns= ['price'], axis= 1, inplace = True)
    except Exception as a:
        traceback.print_exc()
        print(f'No se pudo convertir la columna price a euros por {a}')
    return data

def columna_sim(data):
    '''Función que procesa la columna sim para poder separarla en columnas individuales'''
    
    try:
        df = data.assign(
            cuatro_g = lambda x: x['sim'].str.contains('4G').astype(int),
            ir_blaster = lambda x: x['sim'].str.contains('IR Blaster').astype(int),
            nfc = lambda x: x['sim'].str.contains('NFC').astype(int),
            tres_g = lambda x: x['sim'].str.contains('3G').astype(int),
            wifi = lambda x: x['sim'].str.contains('Wi-Fi').astype(int),
            single_sim = lambda x: x['sim'].str.contains('Single Sim').astype(int),
            volte = lambda x: x['sim'].str.contains('VoLTE').astype(int),
            cinco_g = lambda x: x['sim'].str.contains('5G').astype(int),
            dual_sim = lambda x: x['sim'].str.contains('Dual Sim').astype(int),
            vo_5g = lambda x: x['sim'].str.contains('Vo5G').astype(int)
        )
    except Exception as a:
        traceback.print_exc()
        print(f'No se pudo procesar la columna "sim" por {a}')
    return df