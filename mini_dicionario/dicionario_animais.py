#Aqui fica o dicionário
dicionario_animais = {
    "abelha" : "🐝 Inseto que dá mel",
    "borboleta" : "🦋 Inseto com belas asas",
    "cachorro" : "🐶 Animal que late",
    "dromedalio" : "🐪 Animal que mora no deserto",
    "elefante" : "🐘 Animal com tromba",
    "formiga" : "🐜 Animal conhecido pela sua força de trabalho",
    "galinha" : "🐔 Animal que bota ovo",
    "hipopotamo" : "🦛 Animal grande e conhecido por ser forte nadador",
    "joaninha" : "🐞 Inseto conhecido como símbolo da sorte em algumas culturas",
    "leão" : "🦁 Animal conhecido como rei da selva",
    "macaco" : "🐵 Animal conhecido por comer banana",
    "orangotango" : "🦧 Animal conhecido como primata e pelos seus pelos avermelhados",
    "peixe" : "🐟 Animal que vive no mar",

}

buscar_animal = input(f"""
                      Bem vindo ao DICIONÁRIOS DOS ANIMAIS!
                      Digite um nome de animal para buscar no dicionário: """)
# se a palavra exite no dicionário ele vai mostrar a seguinte mensagem
if buscar_animal in dicionario_animais:
    print(f" {buscar_animal} é {dicionario_animais[buscar_animal]}")
# se a palavra não existe no dicionáeio ela vai mostrar a seguinte palavras
else:
    print(f"Este animal :{buscar_animal} não se encontra no dicionário ❌")