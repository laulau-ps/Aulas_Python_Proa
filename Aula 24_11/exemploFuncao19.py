"""O parâmetro permite que uma função aceite qualquer número de argumentos posicionais.*args

Dentro da função, torna-se uma tupla contendo todos os argumentos passados:args"""

# Acessando argumentos individuais a partir de *args:


def funcao(*args):
    print(
        f"""
    Tipo: {type(args)}
    Primeiro argumento posicional: {args[0]}
    Segundo argumento posicional: {args[1]}
    Todos os argumentos posicionais: {args}
          """
    )


funcao("João", "Maria", "José")
