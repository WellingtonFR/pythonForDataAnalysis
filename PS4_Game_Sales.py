# Libs para Modelagem e Matrizez
import numpy as np
import pandas as pd

# Libs para anaálises gráficas
import matplotlib.pyplot as plt
import seaborn as sns

# Lib para ignorar avisos
import warnings

# Desabilitando avisos
warnings.filterwarnings("ignore")

# Lendo os dados
Base_Dados = pd.read_csv("./csv/PS4_GamesSales.csv", encoding="latin-1")

# Retirando valores nulos
Base_Dados.dropna(inplace=True)

# Verificando
print()
print(Base_Dados.head())
print()

print(Base_Dados.isnull().sum())
print()

print(Base_Dados.describe())
print()

# Retirar os anos
Base_Dados = Base_Dados.loc[(Base_Dados["Year"] != 2019) & (Base_Dados["Year"] != 2020)]
print()

# Verificar
Base_Dados.head()
print()
