import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

Base_dados = pd.read_csv("./csv/StudentsPerformance.csv")

Base_dados.rename(
    columns={
        "gender": "Sexo",
        "race/ethnicity": "Etnia",
        "parental level of education": "Educação dos pais",
        "lunch": "Almoço",
        "test preparation course": "Curso preparatório",
        "math score": "Pontos em matemática",
        "reading score": "Pontos em leitura",
        "writing score": "Pontos em escrita",
    },
    inplace=True,
)

print()
print(Base_dados.head())

print()
print(Base_dados.nunique())

print()
print(f"Valores duplicados:  {Base_dados.duplicated().sum()}")

print()
print(Base_dados["Sexo"].value_counts(normalize=True) * 100)

print()
nivel_de_educacao_dos_pais = (
    Base_dados["Educação dos pais"].value_counts(normalize=True) * 100
)

# print(Base_dados["Educação dos pais"].unique())
# print(nivel_de_educacao_dos_pais)

# plt.figure(figsize=(15, 6))
# plt.title("Nível de educação dos pais")
# plt.xlabel("Nível de educação")
# plt.bar(Base_dados["Educação dos pais"].unique(), nivel_de_educacao_dos_pais)
# plt.xticks(rotation=45, ha="right")
# plt.show()

sns.boxplot(data=Base_dados, x="Pontos em matemática", y="Sexo")
plt.show()

sns.boxplot(data=Base_dados, x="Pontos em leitura", y="Sexo")
plt.show()

sns.boxplot(data=Base_dados, x="Pontos em escrita", y="Sexo")
plt.show()

print()
describe = (
    Base_dados.groupby(by=["Sexo"]).describe()["Pontos em matemática"].reset_index()
)
print(describe)
