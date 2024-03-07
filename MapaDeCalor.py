import pandas as pd
import plotly.express as px

# Cidades
Cidade = [
    "Santo André",
    "São Bernarndo do Campo",
    "Diadema",
    "São Caetano do Sul",
    "Mauá",
    "Ribeirao Pires",
    "Rio Grande da Serra",
    "Sao Paulo",
]

Estado = [
    "São Paulo",
    "São Paulo",
    "São Paulo",
    "São Paulo",
    "São Paulo",
    "São Paulo",
    "São Paulo",
    "São Paulo",
]

# Gerando a Latitude
Latitude = [
    -23.6666,
    -23.6944,
    -23.6865,
    -23.6226,
    -23.6687,
    -23.7141,
    -23.7452,
    -23.5489,
]

# Gerando a Longitude
Longitude = [
    -46.5322,
    -46.5654,
    -46.6234,
    -46.5489,
    -46.4614,
    -46.4137,
    -46.4022,
    -46.6388,
]

# Valor
Vendas = [100, 120, 90, 50, 70, 90, 250, 400]

# Dicionario
Dicionario = {
    "Cidade": Cidade,
    "UF": Estado,
    "Lat": Latitude,
    "Log": Longitude,
    "Vendas": Vendas,
}

Base_Dados = pd.DataFrame(Dicionario)

print(Base_Dados)

# Mapa de Calor Geografico
mapbox = px.density_mapbox(
    data_frame=Base_Dados,
    lat="Lat",
    lon="Log",
    z="Vendas",
    radius=30,
    center=dict(lat=-23.700, lon=-46.5555),
    zoom=8,
    mapbox_style="open-street-map",
)

mapbox.show()
