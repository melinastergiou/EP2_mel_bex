
from funcoes import *
from random import *
from math import *
from dicas import *
from dados_norm import * 

 
#criar documento para impressão colorida e os jogadores etc
print('Bem vindo ao Country Discover!')


# Sorteia Pais e define suas variáveis
pais = sorteia_pais(dados_normalizados)
print(pais)
infopais = dados_normalizados[pais]


l1 = infopais ['geo']['latitude']
p1 = infopais['geo']['longitude']


# Tentativas
tentativas = 20
dicas = [0 , 1 , 2 , 3 , 4 , 5]
mostradica = 'Dicas: '
mostradist = 'Distâncias: '

ptentados = []
# Palpite
palpite = 'melbexlandia'

while palpite != pais:
    #SE ESTÁ TENTANDO O MESMO PAIS
    if palpite in ptentados:
        palpite = input('Qual o seu o palpite? ') 
    else:
        ptentados.append(palpite)

    # Palpite = DICA/DICAS
    if palpite == "dica" or palpite == "dicas":
        # print (mercado de dicas) # fazer mercado de dicas       
        # escolhendo dica!
        dic_escolhida = input("Escolha sua opção {}? ".format(str(dicas)).replace(',', '|'))
        tentativas = num_tentativas(dic_escolhida, tentativas)
        
        if tentativas == False:
            print(mostradist)
            print(mostradica) 
            print('Você não possui tentativas suficientes para essa dica. ')

        else: 
            mostradica += '\n {}'.format(fun_dica(dic_escolhida, infopais))
            dicas = exclui_dicas(dic_escolhida, dicas) 
            print(mostradist)
            print(mostradica) 
            print ('Você tem {} tentativa(s) restante(s)'.format(tentativas))

            
    # Palpite = PAÍS
    elif palpite in dados_normalizados:
        # latitude, longitude pais palpite
        infopalpite = dados_normalizados[palpite]
        p2 = infopalpite["geo"]["longitude"]
        l2 = infopalpite["geo"]["latitude"]
        # distancia de pais --> palpite
        distancia = haversine(EARTH_RADIUS, p1,l1,p2,l2) # tirar casas decimais
        mostradist += '\n {:.3f}km --> {}'.format(distancia, palpite) 
        print(mostradist)
        print(mostradica)       
        tentativas -= 1 
        print ('Você tem {} tentativa(s) restante(s)'.format(tentativas)) 


    elif palpite == "desisto":
        # Caso jogador desista
        p_desistir= input('Tem certeza que deseja desistir?[S/N] ').lower()
        
        if p_desistir == "s":
            print("O país sorteado era {}...".format(pais))
            pergunta = input("Jogar novamente?[S/N] ").lower()
            if pergunta == "s":
                # Sorteia Pais e define suas variáveis -- RECOMEÇA O JOGO
                pais = sorteia_pais(dados_normalizados)
                print(pais)
                infopais = dados_normalizados[pais]

                l1 = infopais ['geo']['latitude']
                p1 = infopais['geo']['longitude']

                # Tentativas
                tentativas = 20
                mostradica = 'Dicas: '
                mostradist = 'Distâncias: '
                dicas = [0 , 1 , 2 , 3 , 4 , 5] 
                ptentados = []


            
            elif pergunta == "n": # ACABA COM O JOGO
                print("É muito deselegante desistir... Até a próxima!")
                break
        
        if p_desistir == "n":
            print("Muito elegante! Bora continuar!")

    palpite = input('Qual o seu o palpite? ')





