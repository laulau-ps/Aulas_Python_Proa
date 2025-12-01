"""Os operadores * e ** também podem ser usados ao chamar funções para desempacotar (expandir) uma lista ou dicionário em argumentos separados.

Desvendando Dicionários com **
Se você tem argumentos de palavras-chave armazenados em um dicionário, pode usar ** para descompactá-los:
"""

def funcao(primeiro_nome, ultimo_nome):
    print(f"Olá {primeiro_nome} {ultimo_nome}")
    
pessoa = {"primeiro_nome": "Laura", "ultimo_nome": "Sena"}

funcao(**pessoa) #mesma coisa que: funcao(primeiro_nome = "Laura", ultimo_nome = "Sena")   

#desempacota o dict e exibe conforme os argumentos