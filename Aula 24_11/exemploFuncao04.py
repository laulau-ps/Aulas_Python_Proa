
''' As funções podem enviar dados de volta para o código que as chamou usando a instrução.return

Quando uma função return  chega a uma instrução, ela para de ser executada e envia o resultado de volta:'''

def saudacao():
    return "Olá de uma função"

mensagem = saudacao()
print(mensagem)

# retornando a função dentro de um print

print(saudacao())