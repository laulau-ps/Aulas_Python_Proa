"""*args é útil quando você quer criar funções flexíveis:
Uma função que calcula a soma de qualquer número de valores:
"""

def funcao_soma_indefinida(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

print(funcao_soma_indefinida(1, 2, 3))    
print(funcao_soma_indefinida(10, 20, 30, 40))    
print(funcao_soma_indefinida(5))     

#repete o laço até que se acabe a quantidade de argumentos presentes na chamada da função