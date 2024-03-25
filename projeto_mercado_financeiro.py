# Libs para Modelagem e Matrizez
import numpy as np
import pandas as pd

# Libs para anaálises gráficas
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# Lib para ignorar avisos
import warnings

# Desabilitando avisos
warnings.filterwarnings("ignore")

# Lendo os dados
Base_Dados = pd.read_excel("./csv/magalu.xlsx")

# Verificando
print()
print(Base_Dados.head())
print()

print()
print(Base_Dados.info())
print()

# Series Temporais
Dados = Base_Dados.set_index("Data")

print()
print(Dados.head())
print()

# Gráfico de linha
# plt.style.use("seaborn-v0_8-darkgrid")
# plt.figure(figsize=(16, 5))
# plt.title("Análise das ações da Magalu - Fechamento", fontsize=15, loc="left")
# plt.plot(Base_Dados["Data"], Base_Dados["Fechamento"])
# plt.xlabel("Período")
# plt.ylabel("Valor da Ação (R$)")
# plt.show()


# Gráfico com médias móveis
# Media_Movel = Dados["Fechamento"].rolling(5).mean()
# Media_Tendencia = Dados["Fechamento"].rolling(30).mean()

# plt.style.use("seaborn-v0_8-darkgrid")
# plt.figure(figsize=(16, 5))
# plt.title("Análise das ações da magalu - Fechamento", fontsize=15, loc="left")

# plt.plot(Dados.index, Dados["Fechamento"])
# plt.plot(Dados.index, Media_Movel)
# plt.plot(Dados.index, Media_Tendencia)

# plt.xlabel("Período da Cotação")
# plt.ylabel("Valor da Ação (R$)")

# plt.show()

# Gráfico de Candlestick
# Grafico = go.Figure(
#     data=[
#         go.Candlestick(
#             x=Dados.index,
#             open=Dados["Abertura"],
#             high=Dados["Maior"],
#             low=Dados["Menor"],
#             close=Dados["Fechamento"],
#         )
#     ]
# )

# Grafico.update_layout(xaxis_rangeslider_visible=False)

# Grafico.show()
