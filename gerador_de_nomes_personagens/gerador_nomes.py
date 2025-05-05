import random

nomes_prefixo = 'astronauta','rei/rainha','princesa/principe','mestre','mago/maga'
nomes_sufixo = 'inteligente','feroz','grande','pequeno','veloz'


nomes_possiveis = ''

nome_meio = input("digite um nome para seu personagem: ")

nome_gerado =''. join(random.choice(nomes_prefixo)+" "+nome_meio+" "+random.choice(nomes_sufixo))


print(f"""
    ===============================================
      O nome gerado foi: {nome_gerado}
    ===============================================

""")

 