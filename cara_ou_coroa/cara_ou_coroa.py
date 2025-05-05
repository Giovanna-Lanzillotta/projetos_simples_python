import random


aposta = input("Você quer cara ou coroa? ")

opcoes = ["cara","coroa"]
jogada = random.choice(opcoes)

if aposta == jogada:
    print(f"🥳 Você ganhou! A jogada foi {jogada}")
else:
    print(f"😓 Você perdeu! A jogada foi {jogada}")
