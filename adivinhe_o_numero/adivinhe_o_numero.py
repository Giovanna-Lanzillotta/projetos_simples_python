import random # random serve para gerar o 

#intervalo dos números
numero_minimo = 0
numero_maximo = 100

# Número de tentativas
tentativas = 0

# A função random.randint() serve para gerar um número inteiro
numero = random.randint(numero_minimo, numero_maximo)

while True:
    palpite = int(input(f"Digite um número entre {numero_minimo} e {numero_maximo} :"))
    tentativas +=1
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

    if tentativas == 5:
        print(f"😯 Acabou a suas chances o número era {numero}")
        break
