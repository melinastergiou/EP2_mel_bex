
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

# PRINTS - Apresentação do jogo
print(BLINK + ' =============================' + RESET)
print(BLINK + '|      '+ MAGENTA + '   Bem vindo ao    '+ RESET +'    |'+RESET)
print(BLINK + '|   '+ MAGENTA +'    Country Discover!  '+RESET+'   | '+RESET)
print(' =============================')
print(BOLD + '        by: Melina & Bex' + RESET + '\n')
# - Regras do jogo:
print('Regras do Jogo e Comandos:')
print('dica/dicas ----> Abre o Mercado de dicas')
print('desisto    ----> Desiste da rodada')
print('inventário ----> Exibe a sua posição\n')


# Tentativas
tentativas = 20
dicas = [0 , 1 , 2 , 3 , 4 , 5] 
mostradica = '\n'+'Dicas: '
mostradist = '\n'+'Distâncias: '

ptentados = []
pchutes = []
coresdica =[]
letrasdica =[]
# Palpite para rodar, tive que fazer esse ser funcional 
palpite = 'melbexlandia' #input('\n'+'Qual o seu o palpite? ')

# CRIANDO WHILE PARA NÃO TER TENTATIVAS NEGATIVAS
    
while palpite != pais and tentativas >= 1:
    palpite = input('\n'+'Qual o seu o palpite? ')
    print(palpite)
    print(pais)
    # SE ESTÁ TENTANDO O MESMO PAIS

    # Mel coloquei essa parte dentro do laço de if que checa se o palpite é um pais, pq ai fica mais proativo
    # if palpite in dados_normalizados:
    #     if palpite in ptentados:
    #         palpite = input('Qual o seu o palpite? ') 
    #     else:
    #         ptentados.append(palpite)
    #         print(ptentados)

    # Palpite = DICA/DICAS
    if palpite == "dica" or palpite == "dicas":
        # print (mercado de dicas) # fazer mercado de dicas       
        # escolhendo dica!
        print(' =============================================')
        print('|'+ MAGENTA +' Mercado de Dicas:             '+RESET+'              |')
        print('| 1. Cor da Bandeira  --> custa 4 tentativas  |')
        print('| 2. Letra da Capital --> custa 3 tentativas  |')
        print('| 3. Área             --> custa 6 tentativas  |')
        print('| 4. População        --> custa 5 tentativas  |')
        print('| 5. Continente       --> custa 4 tentativas  |')
        print('| 0. Desistir da dica                         |')
        print(' =============================================\n')
        dic_escolhida = input("Escolha sua opção {}? ".format(str(dicas)).replace(',', '|'))
        tentativas = num_tentativas(dic_escolhida, tentativas)
        
        if tentativas == False:
            print(mostradist)
            for p in pchutes:
                if p[1] >= 2*(EARTH_RADIUS):
                    print(RED + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)
                elif p[1] < 2*(EARTH_RADIUS) and p[1] >= EARTH_RADIUS:
                    print(YELLOW + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)  
                elif p[1] < EARTH_RADIUS:
                    print(GREEN + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)
            print(mostradica) 
            print(RED + 'Você não possui tentativas suficientes para essa dica. ' + RESET) # COR


        else:
            if fun_dica(dic_escolhida, infopais, dicas) == '':
                print(mostradist)
                for p in pchutes:
                    if p[1] >= 2*(EARTH_RADIUS):
                        print(RED + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)
                    elif p[1] < 2*(EARTH_RADIUS) and p[1] >= EARTH_RADIUS:
                        print(YELLOW + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)  
                    elif p[1] < EARTH_RADIUS:
                        print(GREEN + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)
                print('Você já usou essa dica.')
            elif fun_dica(dic_escolhida, infopais, dicas) ==  RED + '\n Você não possui tentativas suficientes para essa dica. ' + RESET:
                print(mostradist)
                for p in pchutes:
                    if p[1] >= 2*(EARTH_RADIUS):
                        print(RED + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)
                    elif p[1] < 2*(EARTH_RADIUS) and p[1] >= EARTH_RADIUS:
                        print(YELLOW + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)  
                    elif p[1] < EARTH_RADIUS:
                        print(GREEN + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)
                print(fun_dica(dic_escolhida, infopais, dicas))
            elif dic_escolhida == '1':
                i = fun_dica(dic_escolhida, infopais, dicas)
                while i in coresdica:
                    i = fun_dica(dic_escolhida, infopais, dicas) 
                coresdica.append(i)
                mostradica += '\n {}'.format(i)
                print(mostradist)
                for p in pchutes:
                    if p[1] >= 2*(EARTH_RADIUS):
                        print(RED + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)
                    elif p[1] < 2*(EARTH_RADIUS) and p[1] >= EARTH_RADIUS:
                        print(YELLOW + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)  
                    elif p[1] < EARTH_RADIUS:
                        print(GREEN + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)
            elif dic_escolhida == '2':
                b = fun_dica(dic_escolhida, infopais, dicas) 
                while b in letrasdica:
                    b = fun_dica(dic_escolhida, infopais, dicas) 
                letrasdica.append(b)
                mostradica += '\n {}'.format(b)
                print(mostradist)
                for p in pchutes:
                    if p[1] >= 2*(EARTH_RADIUS):
                        print(RED + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)
                    elif p[1] < 2*(EARTH_RADIUS) and p[1] >= EARTH_RADIUS:
                        print(YELLOW + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)  
                    elif p[1] < EARTH_RADIUS:
                        print(GREEN + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)
            else: 
                print(mostradist)
                for p in pchutes:
                    if p[1] >= 2*(EARTH_RADIUS):
                        print(RED + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)
                    elif p[1] < 2*(EARTH_RADIUS) and p[1] >= EARTH_RADIUS:
                        print(YELLOW + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)  
                    elif p[1] < EARTH_RADIUS:
                        print(GREEN + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)
                mostradica += '\n {}'.format(fun_dica(dic_escolhida, infopais, dicas))
                dicas = exclui_dicas(dic_escolhida, dicas) 
                
            print(mostradica) 
            print ('\n'+'Você tem ' + CYAN + '{}'.format(tentativas) + RESET + ' tentativa(s) restante(s)') # COR

    # Palpite = PAÍS
    elif palpite in dados_normalizados:
        # latitude, longitude pais palpite
        infopalpite = dados_normalizados[palpite]
        p2 = infopalpite["geo"]["longitude"]
        l2 = infopalpite["geo"]["latitude"]

        if palpite in ptentados:
            print('Esse país já foi... tente denovo')  
        else: 
            ptentados.append(palpite)
            infopalpite = dados_normalizados[palpite]
            p2 = infopalpite["geo"]["longitude"]
            l2 = infopalpite["geo"]["latitude"]
            # distancia de pais --> palpite
            haversine1 = haversine(EARTH_RADIUS, p1,l1,p2,l2)
            pchutes = adiciona_em_ordem(palpite, haversine1, pchutes) 
            print(mostradist)
            for p in pchutes:
                if p[1] >= 2*(EARTH_RADIUS):
                    print(RED + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)
                elif p[1] < 2*(EARTH_RADIUS) and p[1] >= EARTH_RADIUS:
                    print(YELLOW + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)  
                elif p[1] < EARTH_RADIUS:
                    print(GREEN + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)
            print(mostradica)       
            tentativas -= 1 
            print ('\n'+'Você tem ' + CYAN + '{}'.format(tentativas) + RESET + ' tentativa(s) restante(s)') # COR

    elif palpite == "desisto":
        # Caso jogador desista
        p_desistir= input('\nTem certeza que deseja desistir?[S/N] ').lower()
        
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
                mostradica = '\n'+'Dicas: '
                mostradist = '\n'+'Distâncias: '
                dicas = [0 , 1 , 2 , 3 , 4 , 5] 
                ptentados = []
                pchutes = [] 
                # PRINTS - Apresentação do jogo
                print(' =============================')
                print('|         Bem vindo ao        |')
                print('|       Country Discover!     | ')
                print(' =============================\n')
                # - Regras do jogo:
                print('Regras do Jogo e Comandos:')
                print('dica/dicas ----> Abre o Mercado de dicas')
                print('desisto    ----> Desiste da rodada')
                print('inventário ----> Exibe a sua posição \n')

            elif pergunta == "n": # ACABA COM O JOGO
                print("\nÉ muito deselegante desistir... Até a próxima!")
                break

        if p_desistir == "n":
            print("\nMuito elegante! Bora continuar!")

    elif palpite == 'inventario':
        print(mostradist)
        for p in pchutes:
            if p[1] >= 2*(EARTH_RADIUS):
                print(RED + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)
            elif p[1] < 2*(EARTH_RADIUS) and p[1] >= EARTH_RADIUS:
                print(YELLOW + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)  
            elif p[1] < EARTH_RADIUS:
                print(GREEN + '{:.3f} km --> {}'.format(p[1], p[0]) + RESET)
        print(mostradica)    
    
    # BEEEEX ARRUMEI PALPITE TEM QUE SER QUALQUER COISA PRO NOSSO WHILE RODAR DE NOVO!!! 
    else:
        print(RED + 'Opção inválida' + RESET) # COR

    #palpite = input('\n' + 'Qual o seu o palpite? ')
    


# AQUI TO TENTANDO ESCREVER UM ACABARAM AS TENTATIVAS, PORQUE DAÍ O JOGO TEM QUE RODAR DENOVO COMO SE FOSSE APÓS ACERTO!
if tentativas<=0:
    print ('\nAcabaram as tentativas... O país sorteado era {}'.format(pais))

if pais == palpite:
    print('\nVocê acertou o País!! O pais sorteado era mesmo {}'.format(pais))

voltar = input('Você deseja jogar novamente? (S/N)') 

# JOGANDO NOVAMENTE APÓS ACERTO
#voltar = input('Você deseja jogar novamente? (S/N)')
if voltar == 'S' or voltar == 's':
    pais = sorteia_pais(dados_normalizados)
    print(pais)
    infopais = dados_normalizados[pais]

    l1 = infopais ['geo']['latitude']
    p1 = infopais['geo']['longitude']

    # Tentativas
    tentativas = 20
    mostradica = '\n'+'Dicas: '
    mostradist = '\n'+'Distâncias: '
    dicas = [0 , 1 , 2 , 3 , 4 , 5] 
    ptentados = []
    pchutes = [] 
    # PRINTS - Apresentação do jogo
    print(' =============================')
    print('|         Bem vindo ao        |')
    print('|       Country Discover!     | ')
    print(' =============================\n')
    # - Regras do jogo:
    print('Regras do Jogo e Comandos:')
    print('dica/dicas ----> Abre o Mercado de dicas')
    print('desisto    ----> Desiste da rodada')
    print('inventário ----> Exibe a sua posição \n')
    palpite = input('\n'+'Qual o seu o palpite? ') 

else:
    print(BLUE + 'Fim de jogo. Parabéns!' + RESET) 
        

# PRIORIDADES!


# AJUSTES

# ordem da distância de harversine
# tirar o outras das cores
# append as dicas na ordem que elas aparecem no mercado ? 



