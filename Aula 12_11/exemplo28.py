#laço for - aninhados

""" Um loop aninhado é um loop dentro de um loop.

O "loop interno" será executado uma vez para cada iteração do "loop externo" """

adj = ['vermelha', 'amarela', 'pequena']
frutas = ['maçã', 'banana', 'cereja']

for adjetivo in adj:
    for fruta in frutas:
        print(adjetivo, fruta)