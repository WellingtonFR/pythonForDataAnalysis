# Libs Necessárias

# Libs para Modelagem e Matrizez
import numpy as np
import pandas as pd

# Libs para anaálises gráficas
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Lib para ignorar avisos
import warnings

# Desabilitando avisos
warnings.filterwarnings("ignore")

# Lendo os dados
Base_Dados = pd.read_csv("./csv/Dados_Incendios_Florestais.csv", encoding="utf-8")

# Verificando
print()
print(Base_Dados.head())

# Verifica dados nulos
print()
print(Base_Dados.isnull().sum())

# Estatiticas
print()
print(Base_Dados.describe())

# Info
print()
print(Base_Dados.info())

# Campos unicos
print()
print(Base_Dados.nunique())

# analise por ano dos incendios
Analise = Base_Dados.groupby(by=["year"]).sum().reset_index()

# Tamanho
plt.figure(figsize=(12, 5))

# Style
plt.style.use("ggplot")

# Grafico
plt.title("Total indêncidios no Brasil: 1997 - 2017", loc="left", fontsize=14)
sns.lineplot(
    data=Analise,
    x="year",
    y="number",
    estimator="sum",
    lw=2,
    color="#ff5555",
    alpha=0.85,
)

# Labels
plt.xlabel("Quantidade")
plt.ylabel("Período")

# plt.show()

# analise por ano dos incendios
Analise_02 = Base_Dados.groupby(by=["year", "month"]).sum().reset_index()
Analise_02.head()

# Tamanho
plt.figure(figsize=(12, 5))

# Grafico
plt.title("Indêncidios por mês", loc="left", fontsize=14)
sns.boxplot(
    data=Analise_02,
    x="month",
    y="number",
    palette="coolwarm",
    saturation=1,
    width=0.9,
    linewidth=2,
    order=[
        "Janeiro",
        "Fevereiro",
        "Março",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro",
    ],
)

# Labels
plt.xlabel("Mês")
plt.ylabel("Número de incêndios")

# plt.show()

# analise por ano dos incendios
Analise_03 = (
    Base_Dados.groupby(by=["state"])
    .sum()
    .reset_index()[["state", "number"]]
    .sort_values("number", ascending=False)
)

# Tamanho
plt.figure(figsize=(12, 5))

# Grafico
plt.title("Estados com maior número de incêndios", loc="left", fontsize=14)

# Grafico
plt.bar(Analise_03.state, Analise_03["number"], color="#f44e3f")

# Labels
plt.ylabel("Quantidade")
plt.xticks(rotation=45, ha="right")

# Estados TOP 10
Lista_TOP10 = Analise_03["state"][0:10].values

# Tamanho
plt.figure(figsize=(12, 5))

# Grafico
plt.title("Top 10 Estados com incêncios", loc="left", fontsize=14)

# Loop
for Coluna in Lista_TOP10:

    # Filtrar o estado
    Filtro = Base_Dados.loc[Base_Dados["state"] == Coluna]

    # Agrupar os valores para sumarizar
    Analise_Local = Filtro.groupby(by=["year"]).sum().reset_index()

    # Plot
    sns.lineplot(data=Analise_Local, x="year", y="number", lw=2, alpha=0.85)

# Labels
plt.xlabel("Período")
plt.ylabel("Número de incêndios")

# Legenda
plt.legend(Lista_TOP10, bbox_to_anchor=(1, 0.7))


# Plot Geográfico

# Gerando os estados
Estados = Analise_03.sort_values("state")["state"].values

# Gerando os valores
Valores = Analise_03.sort_values("state")["number"].values

# Latitudes
Lat = [
    -8.77,
    -9.71,
    1.41,
    -3.07,
    -12.96,
    -3.71,
    -15.83,
    -19.19,
    -16.64,
    -2.55,
    -12.64,
    -18.10,
    -7.06,
    -5.53,
    -8.28,
    -8.28,
    -22.84,
    -11.22,
    1.89,
    -27.33,
    -23.55,
    -10.90,
    -10.25,
]

# Longitudes
Log = [
    -70.55,
    -35.73,
    -51.77,
    -61.66,
    -38.51,
    -38.54,
    -47.86,
    -40.34,
    -49.31,
    -44.30,
    -55.42,
    -44.38,
    -35.55,
    -52.29,
    -35.07,
    -43.68,
    -43.15,
    -62.80,
    -61.22,
    -49.44,
    -46.64,
    -37.07,
    -48.25,
]

# Organizados os dados
Dicionario = {
    "Estados": Estados,
    "Latitude": Lat,
    "Longitude": Log,
    "Incêndios": Valores,
}

# Lendo o dicionario
Analise_Geografica = pd.DataFrame(Dicionario)

# Mapa de CAlor Geografico
fig = px.density_mapbox(
    Analise_Geografica,
    lat="Latitude",
    lon="Longitude",
    z="Incêndios",
    radius=30,
    center=dict(lat=-12.700, lon=-46.5555),
    zoom=3,
    mapbox_style="open-street-map",
)

fig.show()
# plt.show()
