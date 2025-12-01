"""O parâmetro permite que uma função aceite qualquer número de argumentos de palavras-chave.**kwargs

Dentro da função, torna-se um dicionário contendo todos os argumentos das palavras-chave:kwargs
"""


def funcao_dados(**minhavar):
    print(f"""
          Tipo: {type(minhavar)}
          Nome: {minhavar['nome']} #exibe o argumento com palavra chave 'nome'
          Idade: {minhavar['idade']} #exibe o argumento com palavra chave 'idade'
          Todos os dados: {minhavar} #exibe todos os argumentos declarados
          """)

funcao_dados(nome = "Laura", idade = 20, cidade = "São Paulo", estado = "SP")    
