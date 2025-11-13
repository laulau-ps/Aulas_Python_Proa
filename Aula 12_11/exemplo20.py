# laço for - break 

''' Com a instrução break, podemos parar o antes de percorrer todos os itens:'''

# exemplo:

frutas = ['maçã','abacaxi','laranja', 'banana', 'cereja']

# print(frutas[2]) = exibe o valor da posição 2 do vetor 'frutas'

for i in frutas:
    print(i)
    if i == 'banana':
        break

#exibe cada dado da variavel 'frutas', até que seja encontrado 'banana'    