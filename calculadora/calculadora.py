def calculadora():
    numero_um = float(input("Digite um numero: "))
    numero_dois = float(input("Digite outro numero: "))

    operacao = (input(f"""
                    Escolha uma operação
                    + - Adição
                    - - Subtração
                    * - Multiplicação
                    / - Divisão
                         """))
    if operacao == "+":
        resultado = numero_um + numero_dois
        print(f'{numero_um} + {numero_dois} = {resultado}')
    
    elif operacao == "-":
        resultado = numero_um * numero_dois
        print(f'{numero_um} - {numero_dois} = {resultado}')
    
    elif operacao == "*":
        resultado = numero_um * numero_dois
        print(f'{numero_um} * {numero_dois} = {resultado}')

    elif operacao == "/":
        resultado = numero_um / numero_dois
        print(f'{numero_um} / {numero_dois} = {resultado}')
    else:
        print("Opção invalida")

calculadora()
