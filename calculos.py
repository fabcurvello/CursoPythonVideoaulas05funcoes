if ( __name__ == "__main__" ):
    print("Esté é o arquivo de funções de cálculos!")

def calcular_media(n1, n2):
    med = (n1 + n2) / 2
    return med


def situacao(media_final, nome):
    if (media_final >= 7):
        sit = "Aprovado"
    else:
        sit = "Reprovado"
    print(f"Nome: {nome} – Média Final: {media_final} - Situação: {sit}")

