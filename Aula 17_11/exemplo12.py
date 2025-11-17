# variavel global alterada na função

x = 'incrivel'
print("Python é", x) #primeira versão da variavel

def minhaFuncao():
    global x #define que a variavel 'x' será global, mesmo sendo reatribuida na função
    
    x = "fantastico" #muda o valor da variavel (respeitando a hierarquia normal de atribuição em variaveis)
    
minhaFuncao() 

print("Python é", x) #segunda versão da variavel
