candidato_a = 0
candidato_b = 0
candidato_c = 0
nulo = 0
branco = 0 

total_eleitores = int(input("Digite o número total de eleitores: "))

for eleitor in range(total_eleitores):
        cpf_eleitor = input("digite o cpf do eleitor: ")
        voto = int(input(f"""Digite o voto
                        1 - canditado_a
                        2 - candidato_b
                        3 - candidato_c
                        0 - branco
                        nulo
                        :"""))
        
# Se o eleitor votar 1 o candidato_a ganha 1 voto
        if voto == 1:
            candidato_a +=1
# Se o eleitor votar 2 o candidato_b ganha 1 voto
        elif voto == 2:
            candidato_b +=1
# Se o eleitor votar 3 o candidato_c ganha 1 voto
        elif voto ==3:
            candidato_c +=1
# Se o eleitor votar 0 o branco ganha 1 voto
        elif voto == 0:
            branco +=1
# Se o eleitor votar em nenhuma das opções acima o nulo ganha 1 voto
        else:
            nulo +=1

# Lógica da porcentagem dos votos
porcentagem_a = (candidato_a/total_eleitores) * 100
porcentagem_b = (candidato_b/total_eleitores) * 100
porcentagem_c = (candidato_c/total_eleitores) * 100
porcentagem_branco = (branco/total_eleitores) * 100
porcentagem_nulo = (nulo/total_eleitores) * 100


# Lógica caso o candidato a venca
if candidato_a > candidato_b and candidato_a > candidato_c:
    resultado = "candidato a ganhou"

# Lógica caso o candidato b venca
elif candidato_b > candidato_a and candidato_b > candidato_c:
    resultado = "candidato b ganhou"

# Lógica caso o candidato c venca
elif candidato_c > candidato_a and candidato_c > candidato_b:
    resultado = "candidato c ganhou"

# Lógica para o segundo turno
if porcentagem_a < 50 and porcentagem_b < 50 and porcentagem_c < 50:
    resultado = "segundo turno"

print(f"""
    NÚMERO DE ELEITORES:{total_eleitores}
    VOTOS CANDIDATO A:{candidato_a} e teve {porcentagem_a:.2f} % dos votos
    VOTOS CANDIDATO B:{candidato_b} e teve {porcentagem_b:.2f} % dos votos
    VOTOS CANDIDATO C:{candidato_c} e teve {porcentagem_c:.2f} % dos votos
    BRANCOS:{branco} e teve {porcentagem_branco:.2f} % dos votos
    NULOS:{nulo} e teve {porcentagem_nulo:.2f} % dos votos

    Resultado: {resultado}
      """)

