"""As funções podem retornar qualquer tipo de dado, incluindo listas, tuplas, dicionários e mais."""


# Uma função que retorna uma lista:
def funcao_lista():
    return ["maçã", "banana", "cereja"]  # retorna uma lista (vetores)


frutas = funcao_lista()  # recebe a lista retornada da função


# exibe o valor do indice da lista definida no 'return' da função (posteriormente armazenado na variavel 'frutas')
print(frutas[0])
print(frutas[1])
print(frutas[2])





# Uma função que retorna uma tupla:
def funcao_tupla():
    return (10, 20)  # retorna uma tupla


x, y = funcao_tupla()  # desempacota a tupla e armazena '10' em 'x' e '20' em 'y'

print("x:", x)  # exibe as variaveis
print("y:", y)
