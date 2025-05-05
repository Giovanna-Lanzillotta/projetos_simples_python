import random

ponto = 0

for partida in range(5):
    aposta = input("Você quer cara ou coroa? ")

    opcoes = ["cara","coroa"]
    jogada = random.choice(opcoes)

    if aposta == jogada:
        print(f"🥳 Você ganhou! A jogada foi {jogada}")
        ponto +=1
    else:
        print(f"😓 Você perdeu! A jogada foi {jogada}")

print(f"A pontuação Final foi: {ponto}")