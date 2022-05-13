
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
print(' =============================')
print('|         Bem vindo ao        |')
print('|       Country Discover!     | ')
print(' =============================\n')

# - Regras do jogo:
print('Regras do Jogo e Comandos:')
print('dica/dicas ----> Abre o Mercado de dicas')
print('desisto    ----> Desiste da rodada')
print('inventário ----> Exibe a sua posição\n')


# Tentativas
tentativas = 20
dicas = [0 , 1 , 2 , 3 , 4 , 5]
mostradica = 'Dicas: '
mostradist = 'Distâncias: '

ptentados = []
# Palpite para rodar, tive que fazer esse ser funcional 
palpite = input('Qual o seu o palpite? ') 

while palpite != pais:
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
        print('| Mercado de Dicas:                           |')
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
            print(mostradica) 
            print(RED + 'Você não possui tentativas suficientes para essa dica. ' + RESET) # COR

        else: 
            mostradica += '\n {}'.format(fun_dica(dic_escolhida, infopais))
            dicas = exclui_dicas(dic_escolhida, dicas) 
            print(mostradist)
            print(mostradica) 
            print ('Você tem ' + CYAN + '{}'.format(tentativas) + RESET + ' tentativa(s) restante(s)') # COR

            
    # Palpite = PAÍS
    elif palpite in dados_normalizados:
        # latitude, longitude pais palpite
        if palpite in ptentados:
            palpite = input('Esse país já foi... tente denovo \nQual o seu o palpite? ') 
        else: 
            ptentados.append(palpite)
            infopalpite = dados_normalizados[palpite]
            p2 = infopalpite["geo"]["longitude"]
            l2 = infopalpite["geo"]["latitude"]
            # distancia de pais --> palpite
            distancia = haversine(EARTH_RADIUS, p1,l1,p2,l2) # tirar casas decimais
            mostradist += '\n {:.3f}km --> {}'.format(distancia, palpite) 
            print(mostradist)
            print(mostradica)       
            tentativas -= 1 
            print ('Você tem ' + CYAN + '{}'.format(tentativas) + RESET + ' tentativa(s) restante(s)') # COR

    elif palpite not in dados_normalizados and palpite!='desisto' and palpite!='dica' and palpite!='dicas':
        print(RED + 'Opção inválida' + RESET) # COR

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
                print("É muito deselegante desistir... Até a próxima!")
                break

        if p_desistir == "n":
            print("Muito elegante! Bora continuar!")

    # BEEEEX ARRUMEI PALPITE TEM QUE SER QUALQUER COISA PRO NOSSO WHILE RODAR DE NOVO!!!    
    palpite = input('Qual o seu o palpite? ') 

print('Você acertou o País!! O pais sorteado era mesmo {}'.format(pais))

# JOGANDO NOVAMENTE APÓS ACERTO
voltar = input('Você deseja jogar novamente? (S/N)')
if voltar == 'S' or voltar == 's':
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
    palpite = input('Qual o seu o palpite? ') 

else:
    print(BLUE + 'Fim de jogo. Parabéns!' + RESET) 
        

# PRIORIDADES!
# Dica não repetível
# caso cores de dica disponíveis acabem!!
# caso letras de capital disponíveis acabem!! --> espina falou de len -- Useiiii
# Arrumar para quando o pais da certo --> esta dando distância de harversine = 0km e não que a pessoa ganhou!! --> resolvi
# o Bo era que o while sempre entrava no primeiro if, pq tinha um or
# botei para o que ja ve se é um pais 


# AJUSTES
# Cor
# LETRA PAÍS, COR PAÍS APPEND COM VÍRGULAS 



