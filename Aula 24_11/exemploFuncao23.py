"""Se você não souber quantos argumentos de palavras-chave serão passados para sua função, adicione dois asteriscos antes do nome do parâmetro.**

Dessa forma, a função receberá um dicionário de argumentos e poderá acessar os itens de acordo:
"""

def funcao(**crianca):
    print(f"Seu sobrenome é: {crianca["ultimo_nome"]}")
    
funcao(primeiro_nome = "Laura", ultimo_nome="Sena")    

#não se sabe quantos argumentos serão recebidos, porém independente disso, o print só retornará o argumento de palavra-chave 'ultimo_nome'