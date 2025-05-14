# Função de inicar o chatbot
def iniciar_chatbot():
    nome = input("Como você gostaria que eu te chamasse? ") #você pede qual nome você gostaria de ser chamado
    print(saudacao())
    while True:
        pergunta_usuario = input(f"{nome}: ") #o nome que você escolheu ficará aparecendo
        resposta_chatbot = opcoes(pergunta_usuario)
        print("🤖 Eureka:", resposta_chatbot)
        if "tchau" in pergunta_usuario.lower() or "adeus" in pergunta_usuario.lower():
            resposta_chatbot = print("😉 Adeus!Qualquer coisa é só me chamar novamente!")
            break

# função de saudação, é uma mensagem de saudação,boas vindas para o usuário
def saudacao():
    return f"Olá eu sou o Eureka um bot de matemática!Como eu posso te ajudar?😁"

# Função que o usuário pode fazer com o chatbot
def opcoes(pergunta):
    pergunta = pergunta.lower()
    if "olá" in pergunta or "oi" in pergunta:
        return saudacao()
    elif "o que você faz?" in pergunta:
        return "eu sou um chatbot de matemática.Ajudo em questões simples de matemática"
    elif "pode me ajudar com uma conta?" in pergunta:
        return contas()  
    elif "Quero definição matemática" in pergunta:
        return outros()
    else:
        return f"""Descupe só atendo em questões matemáticas
        Digite pode me ajudar com uma conta? Caso queira que eu calcule algo
        Digite Quero definição matemática caso Quero alguma definição """


# Caso o usuário peça ajudar para resolver uma csonta e chamada a função contas()
def contas():
    operacao = int(input(f"""Qual operação você gostaria de fazer?
                         1 - Adição
                         2 - Subtração 
                         3 -  Multiplicação
                         4 - Divisão
                         :"""))
    if 1 == operacao:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(resultado)
    elif 2 == operacao:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(resultado)
    elif 3 == operacao:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2 
        print(resultado)
    elif 4 == operacao:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 / num2
        print(resultado) 
    else:
        print("Desculpe essa opção não existe ")
        return opcoes(input(f"Com o que eu posso te ajudar?: "))
        
# Caso o usuário peça outros o chatbot dá a ele outras opções
def outros():
     definicao = int(input(f"""Qual definição você gostaria de saber?
                         1 - Álgebra
                         2 - Geometria
                         3 - Cálculo
                         4 - Probabilidade e Estatística
                         5 - Conjuntos
                         6 - Funções
                         :"""))
# Se o usuário escolher a opção 1,o chatbot vai dar a definição de ÁLGEBRA   
     if definicao == 1:
         return "A álgebra é a parte de matemática que usa símbolos e letras para representar números"
# Se o usuário escolher a opção 2,o chatbot vai dar a definição de GEOMETRIA   
     elif definicao == 2:
         return "A geometria é a parte da matemática que estuda figuras e suas formas e tamanhos e suas propriedades espaciaias"
# Se o usuário escolher a opção 3,o chatbot vai dar a definição de CÁLCULO   
     elif definicao == 3:
        return "O cálculo é a parte da matemática que estuda conceitos como limites,derivadas e integrais,ela é vista na faculdades de exatas"
# Se o usuário escolher a opção 4,o chatbot vai dar a definição de PROBABILIDADE E ESTATÍSTICA
     elif definicao == 4:
         return "A Probabilidade e Estatística é a parte da matemática que estuda a análise de dados e eventos"
# Se o usuário escolher a opção 5,o chatbot vai dar a definição de CONJUNTOS
     elif definicao == 5:
         return "O conjuntos é uma coleção bem definida de objetos chamados de elementos"
# Se o usuário escolher a opção 6,o chatbot vai dar a definição de FUNÇÃO
     elif definicao == 6:
         return "A FUNÇÃO é a relação entre duas variáveis"
# Se o usuário colocar um números diferente de 1 a 6
     else:
        print("Desculpe essa opção não existe ")
        return opcoes(input(f"Com o que eu posso te ajudar?: "))
        

if __name__ == "__main__":
    iniciar_chatbot()