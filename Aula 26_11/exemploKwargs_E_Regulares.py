"""Você pode combinar parâmetros normais com **kwargs.

Parâmetros regulares devem vir antes dos **kwargs:
"""


def funcao_usuario(username, **detalhes):
    print(f"""
    Username: {username} #recebe o argumento regular
    Detalhes a mais: """)   
    for chave, valor in detalhes.items(): #exibe todos os kwargs (referente a 'detalhes')
        print(f"{chave}: {valor}") # chave = nome do argumento | valor = valor do argumento
        
funcao_usuario("laulau123", idade = 20, cidade = "São Paulo", hobby = "Patinar")        
