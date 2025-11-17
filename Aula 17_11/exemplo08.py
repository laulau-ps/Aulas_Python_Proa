# variavel global 

x = "incrivel" #variavel global (esta fora de um escopo)

def minhaFuncao():
    print("Python é " + x) #função usando a variavel global
    
minhaFuncao() #chamando a função   
