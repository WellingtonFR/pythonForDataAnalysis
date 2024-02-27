import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

Base_dados = sns.load_dataset("iris")

# print(Base_dados.head())

# print(Base_dados.shape)

# Medidas de tendência central

# Média
print("")
print("Média")
print(Base_dados["petal_length"].mean())
print("")

# Moda
print("Moda")
print(Base_dados["petal_length"].mode())
print("")

# Mediana
print("Mediana")
print(Base_dados["petal_length"].median())
print("")

# Describe
print("Describe")
print(Base_dados["sepal_length"].describe())
print("")

sns.boxplot(Base_dados["sepal_length"])
plt.show()

# Medidas separatrizes
