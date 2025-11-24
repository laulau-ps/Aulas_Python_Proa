"""*args é útil quando você quer criar funções flexíveis:
Encontrar o valor máximo:
"""

def funcao_valormax(*numeros):
    if len(numeros) == 0:
        return None
    
    maior_valor = numeros[0] #define que o maior valor é o valor de indice 0 da tupla
    
    for num in numeros: #cria um laço para ordenar o maior valor enquanto tiver argumentos na tupla
        if num > maior_valor: #se o num/indice atual for maior que o 'maior_valor'
            maior_valor = num #o 'maior_valor' recebe 'num'
    return maior_valor #retorna o valor da variavel

print(funcao_valormax(1, 2, 3, 40, 8))        