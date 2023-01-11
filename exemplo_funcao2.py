print("Exemplo Função 2:")


def saudacao(nome):
    print(f"Olá!, {nome}")


def calcular_media(n1, n2, nome):
    med = (n1 + n2) / 2
    print(f"Aluno(a): {nome} - Média: {med}")


nome_completo = input("Informe o seu nome completo: ")
nota1 = float(input(f"Informe a Nota 1 de {nome_completo}: "))
nota2 = float(input(f"Informe a Nota 2 de {nome_completo}: "))

saudacao(nome_completo)
calcular_media(nota1, nota2, nome_completo)

print("---FIM---")
