# laço de repetição while - break

# instrução break: para o laço mesmo que a condição ainda for verdadeira

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
    
# enquanto i for menor que 6, exibe i, se i for igual a 3, para o laço, se não, acrescenta (se não acrescentar, o laço se repetirá infinitamente)    