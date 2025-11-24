
''' Você pode atribuir valores padrão aos parâmetros. Se a função for chamada sem argumento, ela usa o valor padrão:'''

def funcao(nome = "aluno"): # parametro com valor padrão definido
    print("Olá", nome)
    
funcao("Laura") #define o argumento a ser exibido     
funcao()      #não define o argumento (exibe o padrão do próprio parametro)
funcao("João")      


