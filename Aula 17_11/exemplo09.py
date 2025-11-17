# variavel local

x = "incrivel" #variavel global (esta fora de um escopo)

def minhaFuncao():
    x = "maravilhoso" #variavel local (dentro do escopo da função)
    print("Python é " + x) #função usando a variavel LOCAL
    
minhaFuncao() #chamando a função com variavel local  

print("Python é ", x) #exibindo a variavel global
