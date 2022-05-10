# FUNÇÕES BASE DO EP2
# Importando bibliotecas
from random import*
from math import * 
from dados import * 

# Função da Dica (sucesso)
def fun_dica(ndica, infopais, tentativas):
  dicas = [0, 1, 2, 3, 4, 5]

  if ndica == '0':
    return print(False), print(tentativas) 
 
  elif ndica == '1' and tentativas >= 2:
    cores_bandeirap = infopais['bandeira']
    lcores = []
    for cor in cores_bandeirap:
      if cores_bandeirap[cor] > 0: 
        lcores.append(cor)

    tentativas -= 4 
    return choice(lcores), tentativas 

  elif ndica == '2' and tentativas >= 3:
    capital = list(infopais['capital'].replace(' ', '').lower())
    tentativas -= 3
    return choice(capital).lower(), tentativas
    
  elif ndica == '3' and tentativas >= 6:
    area = infopais['area']
    tentativas -= 6 
    areap = print('Área: {} km2'.format(area)) ### arrumar no print 
    return area, tentativas  

  elif ndica == '4' and tentativas >= 5:
    pop = infopais['populacao'] 
    tentativas -= 5 
    return pop, tentativas 
  
  elif ndica == '5' and tentativas >= 7: 
    cont = infopais['continente']
    tentativas -= 7
    return cont, tentativas 

  elif int(ndica) not in dicas: 
    return print('Opção inválida')

  else:
    return print('Você não possui tentativas suficientes para essa dica. ')