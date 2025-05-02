# importação do random que gera números aleatórios
import random

# O usuário escolhe o número de partidas
partidas = int(input("Quantas partidas você quer jogar?"))

for partida in range(partidas):
    escolha_usuario = int(input(f"""
                        ESCOLHA 
                        1 - PEDRA
                        2 - PAPEL
                        3 - TESOURA
                        :
                       """))
# A escolha_computador vai ser aleatório de um número entre 1 a 3
    escolha_computador = random.randint(1,3)

# Lógica caso a escolha seja a mesma
    if escolha_usuario == escolha_computador:
        print(f"""EMPATE
            Escolha do computador:{escolha_computador} 
            Sua escolha :{escolha_usuario}""" )

#Lógica do computador vencendo
# computador escolhe pedra e usuario tesoura
    if escolha_computador == 1 and escolha_usuario == 3:
         print(f"""VOCê PERDEU
            Escolha do computador:{escolha_computador} 
            Sua escolha :{escolha_usuario}""" )
# computador escolhe papel e usuario pedra
    elif escolha_computador == 2 and escolha_usuario == 1:
         print(f"""VOCê PERDEU
            Escolha do computador:{escolha_computador} 
            Sua escolha :{escolha_usuario}""" )
# computador escolhe tesoura e usuario papel
    elif escolha_computador == 3 and escolha_usuario == 2:
         print(f"""VOCê PERDEU
            Escolha do computador:{escolha_computador} 
            Sua escolha :{escolha_usuario}""" )

#Lógica do usuário vencendo
# usuário escolhe pedra e computador tesoura
    if escolha_usuario == 1 and escolha_computador == 3:
         print(f"""VOCê GANHOU
            Escolha do computador:{escolha_computador} 
            Sua escolha :{escolha_usuario}""" )
# usuario escolhe papel e computador pedra
    elif escolha_usuario == 2 and escolha_computador == 1:
         print(f"""VOCê GANHOU
            Escolha do computador:{escolha_computador} 
            Sua escolha :{escolha_usuario}""" )
# computador escolhe tesoura e usuario papel
    elif escolha_usuario == 3 and escolha_computador == 2:
         print(f"""VOCê GANHOU
            Escolha do computador:{escolha_computador} 
            Sua escolha :{escolha_usuario}""" )