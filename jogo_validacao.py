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
while palpite != pais:
    # latitude, longitude pais palpite
    infopalpite = dados_normalizados[palpite]
    p2 = infopalpite["geo"]["longitude"]
    l2 = infopalpite["geo"]["latitude"]
    # distancia de pais --> palpite
    distancia = haversine(EARTH_RADIUS, p1,l1,p2,l2) # tirar casas decimais
    print (distancia)
    

    break 

