"""Você pode combinar os dois tipos de argumentos na mesma função.

 Os argumentos anteriores de / são apenas posicionais, e  os argumentos seguintes de * são apenas palavras-chave:"""


def funcao_kwargs_posicionais(a, b, /, *, c, d):
    return a + b + c + d

#os dois primeiros argumentos são posicionais, os dois ultimos são palavra-chave
resultado = funcao_kwargs_posicionais(5, 10, c = 15, d = 20)
print(resultado)
