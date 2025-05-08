# importação da biblioteca time
import time

# Pede ao usuário para escolher um número para comerçar a contagem regressiva
contador = int(input("Digite um número para a contagem regressiva: "))

# usando While, Enquanto o contador for maior que 0,ele faz a contagem com decremento
while contador > 0:
    print(f"⏰ {contador}")
    contador -= 1
    time.sleep(1) # Faz a contagem parar no 1

#Depois que o while acabar mostra a mensagem de fim
print("💫 fim!")