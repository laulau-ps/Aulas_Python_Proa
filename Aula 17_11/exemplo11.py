# variavel global criada na função (palavra chave global)

def minhaFuncao():
    global x #define que a variavel 'x' será global, mesmo tendo sido criada na função
    x = "fantastico"
    
minhaFuncao() 

print("Python é ", x) 
