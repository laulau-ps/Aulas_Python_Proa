
''' Você pode enviar argumentos com a sintaxe chave = valor.'''

def funcao(animal, nome):
    print("Eu tenho um", animal)
    print("Meu", animal, "se chama", nome)  
    
funcao(animal= "gato", nome="Juju") #argumento mesma ordem parametro   

""" Dessa forma, com argumentos por palavras-chave, a ordem dos argumentos não importa. """

funcao(nome="Juju", animal="gato") #argumento ordem diferente do parametro (kwargs)


# A expressão Argumentos de Palavra-Chave é frequentemente abreviada para kwargs na documentação em Python.