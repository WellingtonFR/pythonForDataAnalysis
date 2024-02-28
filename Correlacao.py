# Quando utilizar a correlação
# Quando uma alteração de variável influência outra
# Exemplo: aumento de desconto e aumento de venda / aumento de vendo e aumento de reclamações

# Correlação de Pearson
# Intervalo de -1 a +1, 0 indica que não há correlação

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

Base_dados_full = sns.load_dataset("iris")

Base_dados = Base_dados_full.drop(columns="species")

# print(Base_dados.head())

print()
correlacao = Base_dados.corr()
print(correlacao)
print()

# sns.heatmap(Base_dados.corr(), annot=True)
# plt.show()

sns.scatterplot(data=Base_dados, x="petal_length", y="petal_width")
plt.show()
