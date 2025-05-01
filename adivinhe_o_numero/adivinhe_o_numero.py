import random # random serve para gerar o 

#intervalo dos números
numero_minimo = 0
numero_maximo = 100

# Número de tentativas
tentativas = 5

# A função random.randint() serve para gerar um número inteiro
numero = random.randint(numero_minimo, numero_maximo)

while True:
    palpite = int(input(f"Digite um número entre {numero_minimo} e {numero_maximo} :"))
    tentativas -=1
    print(f"você tem {tentativas} tentativas!")

# O número precisa estar no intervalo entre 0 e 100 senão estiver manda uma mensagem de erro e encerrar
    if palpite < numero_minimo or palpite > numero_maximo:
        print(f"O número precisa ser entre {numero_minimo} e {numero_maximo} ❗")
        break

    # Se o palpite for menor que o número
    elif palpite < numero:
        print("Digite um número maior!")
    # Se o palpite for maior que o número
    elif palpite > numero:
        print("Digite um número menor!")
    # Se o palpite for igual ao número
    elif palpite == numero:
        print("🥳 Parabéns você acertou!")
        break

        # Se as tentativas zerarem o jogo acaba!
    if tentativas == 0:
        print(f"😯 Acabou a suas chances o número era {numero}")
        break
