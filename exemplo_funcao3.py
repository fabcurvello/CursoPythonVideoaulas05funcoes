print("Exemplo Função 3:")


def saudacao(nome):
    print(f"Olá!, {nome}")


def calcular_media(n1, n2):
    med = (n1 + n2) / 2
    return med


def situacao(media_final, nome):
    if (media_final >= 7):
        sit = "Aprovado"
    else:
        sit = "Reprovado"
    print(f"Nome: {nome} – Média Final: {media_final} - Situação: {sit}")


nome_completo = input("Informe o seu nome completo: ")
nota1 = float(input(f"Informe a Nota 1 de {nome_completo}: "))
nota2 = float(input(f"Informe a Nota 2 de {nome_completo}: "))

saudacao(nome_completo)
media = calcular_media(nota1, nota2)
situacao(media, nome_completo)

print("---FIM---")
