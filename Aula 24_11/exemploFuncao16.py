"""Para especificar que uma função pode ter apenas argumentos de palavras-chave, adicione antes dos argumentos:*,"""


def minha_funcao(*, nome): #define que os argumentos passados serão sempre kwargs
    print("Olá", nome)
    
    
minha_funcao(nome="Laura")    #funciona     
minha_funcao("Laura")    #não funciona (pois só aceita argumentos com palavra-chave)
