import time
import datetime
import math
import random
import statistics
import pandas

print("\nHello world\n")

# comentário de uma linha

"""comentário
de
várias
linhas"""

print("Soma", "2+2", "=", 2 + 2)
print("Subtração", "2-2", "=", 2 - 2)
print("Divisão", "2/2", "=", 2 / 2)
print("Multiplicação", "2x2", "=", 2 * 2)
print("Resto", "5%2", "=", 5 % 2)
print("Exponenciação", "2**3", "=", 2**3)

print("")

# Variáveis
nome = "Wellington"
nome_tipado = str("Wellington de Freitas Rocha")

idade = 36
idade_tipada = int(36)

ponto_flutuante = 10.5
ponto_flutuante_tipado = float(10.5)

print(nome_tipado)
print(idade_tipada)
print(ponto_flutuante_tipado, 0)

print("")

# Manipulação de strings
print(nome_tipado[1])
print(nome_tipado[-13:])
print(nome_tipado.replace("e", "u"))
print(nome_tipado.capitalize())
print(nome_tipado.upper())
print(nome_tipado.lower())
split_nome = nome_tipado.split(" ")
print(split_nome[2])
novo_nome = nome_tipado.replace("Freitas", "Rocha")
print(novo_nome)
print(split_nome[2].startswith("Freitas"))
print(split_nome[1].startswith("de"))
print(nome_tipado.endswith("Rocha"))

print("")

# Tipos de dados

##Listas
Lista_1 = ["Laranja", "Maçã", "Banana"]

for fruta in Lista_1:
    print(fruta)

print()

##Tupla - são imutáveis
Tupla_1 = (1, 2, 3, 4, 5)

for numero in Tupla_1:
    print(numero)

print()

##Dicionários
Dicionario_1 = {
    "ID": 1,
    "Nome": "Wellington",
    "Endereço": "Rua Benjamin Franklin nº300",
    "Cidade": "Londrina",
    "Estado": "PR",
}

for chave in Dicionario_1:
    print(chave)

print()

for valor in Dicionario_1.values():
    print(valor)

print()

for chave, valor in Dicionario_1.items():
    print(f"{chave}:{valor}")

print("Quantidade de elementos em Dicionario: " + str(len(Dicionario_1)))
print()

# Pacote datetime

data_atual = datetime.datetime.today().date()

print(data_atual)
print(type(data_atual))

print()

hoje = datetime.datetime.today()
print(hoje)


hoje_somente_data = datetime.datetime.today().date()
print(hoje_somente_data)

data_anterior = datetime.date(1988, 1, 28)
print(data_anterior)


def data_format(received_data, identificador=""):
    if identificador == "":
        return received_data.strftime("%d/%m/%Y")
    else:
        return time.strftime("%d/%m/%Y", received_data)


soma_data = data_atual + datetime.timedelta(weeks=30)
print(data_format(soma_data))

print("")

# Pacote date

print("Aguardando 1 segundos ...")
time.sleep(1)
print("terminado")

agora_datetime = time.localtime()
print(agora_datetime)

print(data_format(agora_datetime, "time"))

data_texto = "21 June, 2021"
print(data_format(time.strptime(data_texto, "%d %B, %Y"), "time"))

print()

tupla = (50, 5, 10, 15, 25, 55)

print("pacote math")
print(min(tupla))
print(max(tupla))
print(pow(2, 5))
print(math.sqrt(4))
print(math.ceil(1.4))
print(math.floor(1.4))
print(math.pi * (pow(2, 2)))

print()

print("Pacote Random")

lista_2 = [1, 2, 3, 4, 5, 6, 7, 8]
lista_3 = ["Batata", "Couve", "Alface", "Beterraba"]
print(random.choice(lista_2))
print(random.choice(lista_3))
print(random.random())  # Valor entre 0 e 1
print(random.randint(1, 1000))

print("Pacote statistic")
lista_4 = [1, 1, 3, 3, 4, 5, 6, 7, 6, 7, 8, 8, 8, 8, 9, 10]
print(sum(lista_4) / len(lista_4))
print(statistics.mean(lista_4))
print(statistics.median(lista_4))
print(statistics.mode(lista_4))

print()


# Classes
class Pessoa:

    # Construtor
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade

    def boas_vindas(self):
        print(f"Olá, seja bem vindo {self.Nome}")

    def recusado(self):
        print("Acesso recusado")

    def maior_idade(self):
        if self.Idade >= 18:
            print(f"{self.Nome} é maior de idade")
            self.boas_vindas()
        else:
            print("Menor de idade")
            self.recusado()


Odemir = Pessoa("Odemir", 27)

Odemir.maior_idade()
