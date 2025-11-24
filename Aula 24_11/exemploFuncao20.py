"""Usando *args com argumentos regulares
Você pode combinar parâmetros regulares com *args.

Parâmetros regulares devem vir antes dos *args:"""

#saudacao é o primeiro argumento, enquanto tudo que vier após ela, será o argumento 'nomes' (qtde indefinida)
def funcao_reg_args(saudacao, *nomes):
    for nome in nomes:
        print(saudacao, nome)

#'olá' é atribuido ao 'saudacao', enquanto 'jose, joao e maria' ficam em 'nomes'
funcao_reg_args("Olá", "José", "João", "Maria")