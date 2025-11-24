"""Mais exemplos de funções com tupla"""


def funcao_temperatura():
    return (10, 20, 30, 40)  # tupla


temp1, temp2, temp3, temp4 = funcao_temperatura()
# cada variavel receberá o valor da tupla lá do return (na mesma ordem)

print(f"""
    Temperatura 1: {temp1}
    Temperatura 2: {temp2}
    Temperatura 3: {temp3}
    Temperatura 4: {temp4}
      """)
