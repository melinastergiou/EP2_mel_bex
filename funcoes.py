# FUNÇÕES BASE DO EP2
# Importando bibliotecas
from random import*
from math import * 
from dados import * 

# Normalizando bases de países (sucesso)


def normaliza_bp(DADOS):
    bpaises = {}

    for continente in DADOS:
        pcont = DADOS[continente]
        for pais in pcont:
            infop = pcont[pais]
            infop['continente'] = continente

            bpaises[pais] = infop 

    return bpaises 

dados_normalizados = normaliza_bp(DADOS)

# Sorteando paises (sucesso)
def sorteia_pais(dicp):
  paises = list(dicp.keys())

  psort = choice(paises)

  return psort

# Distância de Harversine (sucesso)
def haversine(raio, p1, l1, p2, l2):
  p1 = radians(p1) # latitude pais 1
  p2 = radians(p2) # latitude pais 2
  l1 = radians(l1) # longitude pais 1 
  l2 = radians(l2) # longitude pais 2 

  a = sin((p2-p1)/2)**2
  b = cos(p1)*cos(p2)
  c = sin((l2-l1)/2)**2 

  raiz = sqrt(a + (b*c))

  distancia = 2*raio*asin(raiz)

  return distancia 

# Adicionando em uma Lista Ordenada (sucesso)
def adiciona_em_ordem(pais, distancia, listapd):
    elemento = [pais, distancia]
    
    if len(listapd) == 0:
        listapd.append(elemento)
    
    i = 0 
    for p in listapd:
        if pais == p[0]:
            return listapd 

        elif distancia < p[1]:
            listapd.insert(i, elemento)
            return listapd 

        i += 1 

    listapd.append(elemento)
    return listapd 


# Está na Lista? (sucesso)
def esta_na_lista(pais, listap):
  for p in listap:
    if p[0] == pais:
      return True 
  
  return False 

# Sorteia Letra com Restrições (sucesso)

def sorteia_letra (palavra, restritas):
    cespecial = ['.', ',', '-', ';', ' ']
    nl = cespecial + restritas
    palavra = palavra.lower()
    for np in nl:
        palavra = palavra.replace(np, '')
    if len(palavra) == 0:
        return ''
    return choice(palavra[randint(0, len(palavra)-1)])





