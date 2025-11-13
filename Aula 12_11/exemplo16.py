# laço de repetição while - continue

# instrução continue: pula a interação atual e continua para a proxima dentro do laço

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    
# enquanto i for menor que 6, exibe i, se i for igual a 3, para o laço, se não, acrescenta (se não acrescentar, o laço se repetirá infinitamente)    