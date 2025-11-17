# atribuir valores a variaveis

#varias variaveis, com o mesmo valor:

minhavar = minha_var = _minha_var = minhaVar = MINHAVAR = minhavar2 = Minhavar = MinhaVar = "Olá"

print(minha_var, minhaVar, minhavar2, _minha_var) #todas elas terão o mesmo valor


#varias variaveis, com valores diferentes, declaradas em linha:

x, y, z = "Um", "Dois", "Três"
print(x, y, z)

#receber um caractere por variavel, de uma string:
x, y,z = "ola" #cada letra ficará armazenada em uma variavel
print(x)
