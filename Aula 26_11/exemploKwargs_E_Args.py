"""Você pode usar tanto *args quanto **kwargs na mesma função.

A ordem deve ser:

parâmetros regulares
*args
**kwargs
"""


def funcao(titulo, *args, **kwargs):
    print(f"""
          Título: {titulo} #exibe o argumento regular
          Argumentos posicionais: {args} #exibe os argumentos posicionais
          Argumentos palavra-chave: {kwargs} #exibe os argumentos palavra-chave (dict)
          """)
    
funcao("User info", "Laura", "João", "Maria", idade = 20, cidade = "São Paulo", hobby = "Dança")