from funcoes import *
from random import *
from math import * 
#criar documento para impressão colorida e os jogadores etc
print('Bem vindo ao Country Discover!')


# Sorteia Pais e define suas variáveis
pais = sorteia_pais(dados_normalizados)
infopais = dados_normalizados[pais]
print(infopais.keys())

l1 = infopais ['geo']['latitude']
p1 = infopais['geo']['longitude']


# Tentativas
tentativas = 20

# Palpite
palpite = input('Qual o seu o palpite? ')

