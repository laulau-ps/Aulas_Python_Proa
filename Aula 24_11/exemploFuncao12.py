
''' Você pode enviar qualquer tipo de dado como argumento para uma função (string, número, lista, dicionário, etc.).

O tipo de dado será preservado dentro da função:'''

# Enviando uma lista (vetores) como argumento:
def funcao_exibir_frutas(lista_das_frutas): #função que exibe uma lista de frutas (definida nos parametros)
    for fruta in lista_das_frutas: #procura pelas frutas na lista de frutas
        print(fruta) #exibe o nome da fruta
    
minhas_frutas = ['maçã', 'banana', 'cereja'] #variavel da lista de frutas

funcao_exibir_frutas(minhas_frutas)  #envia a lista 'minhas_frutas' como argumento para que a função funcione  



# Enviando um dicionário (matriz / trata como objeto) como argumento:
def funcao_com_dicionario(pessoa):
    print("Nome:", pessoa["nome"]) #exibe o resultado do argumento de chave 'nome' no dict
    print("Idade:", pessoa["idade"]) #exibe o resultado do argumento de chave 'idade' no dict
    
minha_pessoa = {"nome": "Laura",  # chave 'nome' valor 'Laura'
                "idade": "20 anos"
                }  # chave 'idade' valor '20 anos' 
funcao_com_dicionario(minha_pessoa) #argumentos presentes no dict 'minha_pessoa'




