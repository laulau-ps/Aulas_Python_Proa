
''' Quando você chama uma função com argumentos sem usar palavras-chave, elas são chamadas de argumentos posicionais.

Argumentos posicionais devem estar na ordem correta:'''

def funcao(animal, nome):
    print("Eu tenho um", animal)
    print("Meu", animal, "se chama", nome)  
    
funcao("gato","Juju") #argumento mesma ordem parametro (posicional)  
 
funcao("Juju","gato") # erro (vai exibir o nome no lugar do parametro 'animal') 



