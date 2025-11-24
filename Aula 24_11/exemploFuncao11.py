
''' Você pode misturar argumentos posicionais e de palavras-chave em uma chamada de função.

No entanto, argumentos posicionais devem vir antes dos argumentos de palavras-chave:'''

def funcao(animal, nome, idade):
    print("Eu tenho um", animal, "de", idade, "anos, chamado",nome)
    
funcao("gato", idade="2", nome="Juju")    
    
    




