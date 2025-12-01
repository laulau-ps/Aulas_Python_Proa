"""Os operadores * e ** também podem ser usados ao chamar funções para desempacotar (expandir) uma lista ou dicionário em argumentos separados.

Listas de Desempacotamento com *
Se você tem valores armazenados em uma lista, pode usar * para descomapontá-los em argumentos individuais:
"""

def funcao(a, b, c):
    return a + b + c

numeros = [1, 2, 3] #lista de números

resultado = funcao(*numeros) #desempacota a lista 'numeros' e direciona cada valor como um argumento
print(resultado)
