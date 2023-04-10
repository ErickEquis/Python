import pandas as pd
import numpy as np

dataPemex = pd.read_csv("DAESOPS.csv") #Cargando BBDD
dataPemex = dataPemex.transpose() #Transponiendo
print(dataPemex.iloc[[0,1],[10,27]]) #Muestra la fila y columnas
dataPemex.rename({'Cambiar':'CambiodelCambio'}, axis=10)
print(dataPemex.iloc[[0,1],[10,27]])