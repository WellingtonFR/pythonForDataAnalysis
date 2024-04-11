import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Definir tema
sns.set_theme(style="darkgrid")

# Dados
Base_dados = sns.load_dataset("tips")

# print()
# print(Base_dados.head())
# print()

Base_dados.rename(
    columns={
        "total_bill": "Valor final",
        "tip": "Gorjeta",
        "sex": "Sexo",
        "smoker": "Fumante",
        "size": "Pessoas na mesa",
        "day": "Dia",
        "time": "Período",
    },
    inplace=True,
)

# print()
# print(Base_dados.head())
# print()

# Gráfico relplot
# sns.relplot(x="Valor final", y="Gorjeta", data=Base_dados)

# Passando outro parâmetro como classe
# sns.relplot(x="Valor final", y="Gorjeta", data=Base_dados, hue="Sexo")

# Gráfico de linha com 2 eixos
# sns.relplot(x="Valor final", y="Gorjeta", data=Base_dados, kind="line", hue="Fumante")

# Gráfico hisplot
# sns.histplot(data=Base_dados, x="Valor final", hue="Fumante")

# Gráfico barplot
# sns.barplot(data=Base_dados, x="Sexo", y="Valor final", hue="Fumante")

# Pair plot (múltiplos gráficos)
# sns.pairplot(data=Base_dados, hue="Sexo")
# sns.pairplot(data=Base_dados, kind="kde", hue="Fumante")

# Boxplot
sns.boxplot(data=Base_dados, x="Dia", y="Valor final", hue="Sexo")

plt.show()
