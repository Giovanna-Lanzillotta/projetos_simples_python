import random


quantidade_caracteres = int(input("Qual a quantidade de caracteres: "))

def gerador_senhas():
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '0123456789'
    simbolos = '!@#$%^&*()_+=-`~[]\|;:,./<>?'

    caracteres_possiveis = ''

    if minusculas:
        caracteres_possiveis += minusculas
    if maiusculas:
        caracteres_possiveis += maiusculas
    if numeros:
        caracteres_possiveis += numeros
    if simbolos:
        caracteres_possiveis += simbolos

    senha_gerada = ''.join(random.choice(caracteres_possiveis) for _ in range(quantidade_caracteres))
    print("Senha gerada:", senha_gerada)

if __name__ == "__main__":
    gerador_senhas()
