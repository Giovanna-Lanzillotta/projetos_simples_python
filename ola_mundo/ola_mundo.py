# importação do datetime para fornecer data e hora
import datetime 


nome = input("Digite seu nome: ")
# data e hora estão na variável agora
agora = datetime.datetime.now()
#pega somente o dia
dia_atual = agora.day

#pega somente o mês
mes_atual = agora.month

#pega somente o ano
ano_atual = agora.year

#pega somente a hora
hora_atual = agora.hour

#pega somente minuto
minuto_atual = agora.minute

print(f"""
      !!! Olá mundo e olá {nome}! 
      Bem-vindo!
      Hoje é {dia_atual}/{mes_atual}/{ano_atual}
      e são {hora_atual}:{minuto_atual}
      """)