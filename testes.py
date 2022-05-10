from funcoes import *
from random import *
from math import *

pais = sorteia_pais(dados_normalizados)
infopais = dados_normalizados[pais]
tentativas = 20 

print(fun_dica(0, infopais, tentativas))