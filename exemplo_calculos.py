import calculos

nome = input("Digite o seu nome: ")
nota1 = float(input("Digite a Nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = calculos.calcular_media(nota1, nota2)
print(f"Sua média é {media}")

calculos.situacao(media, nome)
