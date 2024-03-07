import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings

warnings.filterwarnings("ignore")

Base_Dados = pd.read_csv("./csv/unicorns till sep 2022.csv")

Base_Dados.rename(
    columns={
        "Company": "Empresa",
        "Valuation ($B)": "Valor ($)",
        "Date Joined": "Data de Adesão",
        "Country": "Pais",
        "City": "Cidade",
        "Industry": "Setor",
        "Investors": "Investidores",
    },
    inplace=True,
)

# Conversão para Data
Base_Dados.insert(0, "Id", range(1, len(Base_Dados) + 1))
Base_Dados["Data de Adesão"] = pd.to_datetime(Base_Dados["Data de Adesão"])
Base_Dados["Mes"] = pd.DatetimeIndex(Base_Dados["Data de Adesão"]).month
Base_Dados["Ano"] = pd.DatetimeIndex(Base_Dados["Data de Adesão"]).year
Base_Dados["Valor ($)"] = pd.to_numeric(
    Base_Dados["Valor ($)"].apply(lambda Linha: Linha.replace("$", ""))
)

Analise = round(Base_Dados["Pais"].value_counts(normalize=True) * 100, 1)

print()
print(Base_Dados.head())
print()

# Valores Unicos do setor
# print()
# print(Base_Dados["Setor"].unique())
# print()

# Valores Unicos - Rank
# print()
# print(Base_Dados["Setor"].value_counts())
# print()

# Tabela Analitica
Analise_Agrupada = (
    Base_Dados.groupby(by=["Empresa", "Ano", "Valor ($)", "Pais"])
    .count()["Id"]
    .reset_index()
    .sort_values(by="Valor ($)", ascending=False)
)

print()
print(Analise_Agrupada)
print()

print()
print(Analise_Agrupada.loc[Analise_Agrupada["Pais"] == "Brazil"])
print()

# plt.figure(figsize=(15, 6))
# plt.title("Analise dos Setores")
# plt.bar(Base_Dados["Setor"].value_counts().index, Base_Dados["Setor"].value_counts())
# plt.xticks(rotation=45, ha="right")
# plt.show()

# # Plot geral dos Paises

# plt.figure(figsize=(15, 6))
# plt.title("Analise dos Paises gerador de Unicornios")
# plt.pie(Analise, labels=Analise.index, shadow=True, startangle=90, autopct="%1.1f%%")
# plt.show()

# Plot geral dos Paises top 10
# plt.figure(figsize=(15, 6))
# plt.title("Analise dos Paises gerador de Unicornios - Top 10")
# plt.pie(
#     Analise.head(10),
#     labels=Analise.index[0:10],
#     shadow=True,
#     startangle=90,
#     autopct="%1.1f%%",
# )
# plt.show()
