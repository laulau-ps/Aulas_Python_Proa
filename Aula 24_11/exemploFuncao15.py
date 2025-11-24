"""Você pode especificar que uma função pode ter APENAS argumentos posicionais.

Para especificar argumentos apenas posicionais, adicione após os argumentos:, /"""


def minha_funcao(nome, /): #define que os argumentos passados serão somente posicionais
    print("Olá", nome)
    
minha_funcao("Laura")    #funciona
minha_funcao(nome="Laura")    #não funciona (pois só aceita argumentos posicionais)