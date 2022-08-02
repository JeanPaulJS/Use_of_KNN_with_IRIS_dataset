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