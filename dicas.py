# FUNÇÕES BASE DO EP2
# Importando bibliotecas
from cgitb import reset
from random import*
from math import * 
from dados import * 

# CORES
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m" 
YELLOW = "\033[;33m"
MAGENTA = "\033[;35m"


# Função da Dica (sucesso)
def fun_dica(ndica, infopais, dicas):
  x = int(ndica)
  
  if x not in dicas:
    return ''
  else:
    if ndica == '0':
      return ''

    elif ndica == '1':
      cores_bandeirap = infopais['bandeira']
      lcores = []
      for cor in cores_bandeirap:
        if cores_bandeirap[cor] > 0: 
          lcores.append(cor)

      return '- Cores da Bandeira: {}'.format(choice(lcores)) 

    elif ndica == '2' :
      capital = list(infopais['capital'].replace(' ', '').lower())
      a = choice(capital) # tentei arrumar aqui mel
      i = capital.index(a)
      capital.pop(i)
      return "- Letras da capital: {}".format(a.lower())

    elif ndica == '3':
      area = infopais['area']
      return '- Área: {:,} km2'.format(area).replace(",",".") 

    elif ndica == '4':
      pop = infopais['populacao'] 
      return  "- População: {:,} habitantes".format(pop).replace(",",".")
    
    elif ndica == '5': 
      cont = infopais['continente']
      return  "- Continente: {}".format(cont)
    
    else:
      return RED + 'Você não possui tentativas suficientes para essa dica. ' + RESET

def num_tentativas(ndica, tentativas):

  if ndica == '1':
    tentativas -= 4
  elif ndica == '2':
    tentativas -= 3
  elif ndica == '3':
    tentativas -= 6
  elif ndica == '4':
    tentativas -= 5
  elif ndica == '5':
    tentativas -= 7

  if tentativas >= 0:
    return tentativas

  return False 

def exclui_dicas(ndica, dicas):
  x = int(ndica)
  if x not in dicas: 
    return dicas 
  else:
    if ndica == '3':
      x = dicas.index(3)
      del(dicas[x])
    elif ndica == '4':
      x = dicas.index(4)
      del(dicas[x])
    elif ndica == '5':
      x = dicas.index(5)
      del(dicas[x])
    return dicas 

def cor_haversine(distancia, EARTH_RADIUS):
  
  

  if distancia >= 2*(EARTH_RADIUS):
    return RED + '{:.3f}'.format(distancia) + " Km" + RESET
  elif distancia <= (3/4)*(2*EARTH_RADIUS) and distancia>= (EARTH_RADIUS):
    return YELLOW + '{:.3f}'.format(distancia) + " Km" + RESET
  elif distancia < (EARTH_RADIUS) and distancia>= (3/4)*(EARTH_RADIUS):
    return MAGENTA + '{:.3f}'.format(distancia) + " Km" + RESET 
  elif distancia < (3/4)*(EARTH_RADIUS):
    return GREEN + '{:.3f}'.format(distancia) + " Km" + RESET


#def ordem_haversine(distancia):

    