# Exemplo inicial, sem utilizar o recurso de múltiplos parâmetros em funções
def somar(n1, n2, n3):
    total = n1 + n2 + n3
    return total


# Exemplo utilizando o recurso de múltiplos parâmetros em funções
def somar_multiplos_parametros(*numeros):
    total = 0
    for numero in numeros:
        total += numero  # total = total + numero
    return total


print(somar(1, 1, 1))
print(somar_multiplos_parametros(1, 1, 1))
print(somar_multiplos_parametros(1, 1, 1, 1, 1, 1, 1))


