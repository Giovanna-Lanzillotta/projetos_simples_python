#O usuário digita um número inteiro para verificar se ele é par ou ímpar
numero = int(input("Digite um número inteiro: "))
#Se o número for maior que zero ele faza verificação
if numero > 0:
    # Se o resto da divisão do número for 0 ele é par
    if numero % 2 == 0:
        print(f"O número {numero} é par!")
    # senão ele é impar
    else:
        print(f"O número {numero} é impar!")
else:
    print("O número digitado não é um número inteiro")