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
# print("")
# print("Média")
# print(Base_dados["petal_length"].mean())
# print("")

# # Moda
# print("Moda")
# print(Base_dados["petal_length"].mode())
# print("")

# # Mediana
# print("Mediana")
# print(Base_dados["petal_length"].median())
# print("")

# Describe
print("Describe")
print(Base_dados["sepal_length"].describe())
print("")

# sns.boxplot(Base_dados["sepal_length"])
# plt.show()

# Medidas de dispersão

# Amplitude_total = Base_dados["sepal_length"].max() - Base_dados["sepal_length"].min()
# print("Ampliturade total: diferença entre o maior o menor valor observado")
# print(Amplitude_total)
# print()

# Amplitudade_interquartirica = (
#     Base_dados["sepal_length"].describe()[6:7].values
#     - Base_dados["sepal_length"].describe()[4:5].values
# )

# print("Amplitude interquartírica: diferença entre o terceiro e o primeiro quartil")
# print(Amplitudade_interquartirica)
# print()

# Amplitudade_semi_interquartirica = (
#     Base_dados["sepal_length"].describe()[6:7].values
#     - Base_dados["sepal_length"].describe()[4:5].values
# ) / 2

# print("Amplitude semi-interquartírica: média da diferença entre a mediana e os quartis")
# print(Amplitudade_semi_interquartirica)
# print()

# variancia = Base_dados["sepal_length"].var()
# print("Variância: mostra quão distantes os valores estão da média")
# print(variancia)
# print()

# desvio_padrao = Base_dados["sepal_length"].std()
# print(
#     "Desvio padrão: o resultado positivo da raiz quadrada da variância, quanto mais próximo de 0 mais homogêneos são os dados"
# )
# print(desvio_padrao)
# print()

# Medidas de simetria
# Indicador de formas de distribuição dos dados

# Simétrica: média = mediana = moda ou As=0
# Assimétrica negativa: se média < mediana < moda ou As < 0
# Assimétrica positiva: se moda < mediana < média ou As > 0

Base_dados["sepal_length"].skew()
sns.kdeplot(Base_dados["sepal_length"])
plt.show()

# Medidas de curtose: grau de achatamento da distribuição

# Leptocúrtica:
# Mesocúrtica:
# Platicúrtica:
