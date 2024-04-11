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

# Verificar
# print(Base_Dados.head())
# print()

# mais_vendidos = Base_Dados.loc[Base_Dados["Global"] >= 10]

# print(mais_vendidos)

# plt.figure(figsize=(15, 6))
# plt.title("Jogos mais vendidos no mundo")
# plt.pie(
#     mais_vendidos["Global"],
#     labels=mais_vendidos["Game"],
#     startangle=90,
#     autopct="%1.1f%%",
# )
# plt.show()

Analise = Base_Dados.groupby(by=["Year"]).sum().reset_index()


# analisando a proporção dos 100% de cada continemente comparado ao Total
America = [
    America / Total * 100
    for America, Total in zip(Analise["North America"], Analise["Global"])
]
Europa = [
    Europa / Total * 100 for Europa, Total in zip(Analise["Europe"], Analise["Global"])
]
Japao = [
    Japao / Total * 100 for Japao, Total in zip(Analise["Japan"], Analise["Global"])
]
Mundo = [
    Mundo / Total * 100
    for Mundo, Total in zip(Analise["Rest of World"], Analise["Global"])
]

# Tamanho
# plt.figure(figsize=(10, 5))

# # LArgura barra no gráfico
# Largura_Barra = 0.85
# Rotulos = Analise["Year"]
# Grupos = [0, 1, 2, 3, 4, 5]

# # titulo
# plt.title("Análise distribuição por continentes")

# # Plot da America
# plt.bar(Grupos, America, width=Largura_Barra, color="#b5ffb9", edgecolor="white")

# # Plot da Europa
# plt.bar(
#     Grupos,
#     Europa,
#     bottom=America,
#     width=Largura_Barra,
#     color="#f9bc86",
#     edgecolor="white",
# )

# # Plot do Japao
# plt.bar(
#     Grupos,
#     Japao,
#     bottom=[A + B for A, B in zip(America, Europa)],
#     width=Largura_Barra,
#     color="#a3acff",
#     edgecolor="white",
# )

# # Plot do Resto do mundo
# plt.bar(
#     Grupos,
#     Mundo,
#     bottom=[A + B + C for A, B, C in zip(America, Europa, Japao)],
#     width=Largura_Barra,
#     color="#d3acfe",
#     edgecolor="white",
# )

# # Labels
# plt.xticks(Grupos, Rotulos)
# plt.xlabel("Grupo")
# plt.ylabel("Distribuição %")

# # Legenda
# plt.legend(
#     ["America N", "Europa", " Japão", "Mundo"],
#     loc="upper left",
#     bbox_to_anchor=(0.15, -0.1),
#     ncol=4,
# )

# plt.show()


from sklearn.preprocessing import LabelEncoder

Funcao_Label = LabelEncoder()

Base_Dados["Produtor"] = Funcao_Label.fit_transform(Base_Dados["Publisher"])
Base_Dados["Genero"] = Funcao_Label.fit_transform(Base_Dados["Genre"])
Base_Dados["Jogo"] = Funcao_Label.fit_transform(Base_Dados["Game"])

print(Base_Dados)
