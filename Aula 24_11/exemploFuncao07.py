
''' Por padrão, uma função deve ser chamada com o número correto de argumentos.

Se sua função espera 2 argumentos, você deve chamá-la com exatamente 2 argumentos.'''

def funcao_nomes(primeiro_nome, ultimo_nome): # parametro
    print(primeiro_nome , ultimo_nome)
    
funcao_nomes("Laura", "Silva") # argumento   
funcao_nomes("João", "Souza")    
funcao_nomes("Maria") #chamada errada, com apenas 1 argumento   


