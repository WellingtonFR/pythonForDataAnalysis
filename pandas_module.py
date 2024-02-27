import numpy as np
import pandas as pd

pd.set_option("display.max_rows", None)

df = pd.read_csv("./csv/StudentsPerformance.csv")

print(df)

# print(type(df))

# 5 primeiras linhas
# print(df.head())

# 5 últimas linhas
# print(df.tail())

# Quantidade de linhas e colunas
# print(df.shape)

# Nome das colunas
# print(df.columns)

# Verifica duplicadas
# print(df.duplicated())

# Verifica duplicadas
# print(df.duplicated().sum())

# print(df.info())

# Verifica a existência de Nan
# print(df.isna().sum())

# Sumário estatístico para colunas numéricas
# print(df.describe())

# sumário estatístico - inclusive para as variáveis categóricas
# print(df.describe(include="all"))

# quantidade de valores únicos em cada coluna
# print(df.nunique())

# valores únicos
# print(df["parental level of education"].unique())

# frequência entre os gêneros
# print(df.gender.value_counts())

provas = ["math score", "reading score", "writing score"]

# df

df.sort_values(["math score"]).reset_index(drop=True)

# ordena o dataset
df = df.sort_values(by=provas, ascending=False).reset_index(drop=True)

# coluna com a média das provas
df["mean"] = df[provas].mean(axis=1)

# print(df.head())

# consulta
# print(
#     df.query(
#         '(gender == "male") & (`test preparation course` == "none") & (`math score` >= 70)'
#     )
# )

# print(
#     df[
#         (df.gender == "male")
#         & (df["test preparation course"] == "none")
#         & (df["math score"] >= 70)
#     ]
# )

# print(
#     df.loc[
#         (df.gender == "male")
#         & (df["test preparation course"] == "none")
#         & (df["math score"] >= 70)
#     ]
# )

# agrupamento - agrupa os dados por gênero e obtém estatísticas descritivas
resultado = df.groupby(by="gender")[provas].agg(["mean", "median"]).T

resultado.to_csv("groupByGenderApplyingMeanAndMedian.csv", index=True)
