#Importar las librerias
import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

#Leer la dataset
iris = pd.read_csv("iris.csv")
iris.head(20)
#puedes usar "iris.tail() para ver las ultimas 5 filas de tu dataset"

iris.shape
iris["species"].value_counts()
#vemos las columnas y valores del dataset resumidas
iris.columns
iris.values
#Pedimos un resumen de los datos del dataset
iris.info()
iris.describe(include='all')
