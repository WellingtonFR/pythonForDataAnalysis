# lib para http
import requests

# Lib para minerar os dados da pagina
from bs4 import BeautifulSoup

# Lib para modelagem de dados
import pandas as pd

# Lib para análise gráfica
import plotly.graph_objects as Dash

# URL para buscar os dados
Site = "https://www.ssp.sp.gov.br/estatistica/violencia-contra-a-mulher"

# Carregar os dados da pagina
Pagina = requests.get(Site)

Coleta = BeautifulSoup(Pagina.text, "html.parser")

# Pegando título da página
print(Coleta.title)

# Localizando as tabelas pela classe
Tabelas = Coleta.find_all("table", attrs={"class": "table table-striped table-hover"})

# Vericando
print(f"Foi localizado { len(Tabelas) } tabelas")
