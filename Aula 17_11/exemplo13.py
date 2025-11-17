#funções são blocos de código, que só são executados quando chamados

#os nomes seguem as mesmas regras das variaveis

#tornam o código orientado a objeto, crie uma vez, utilize quantas vezes quiser

#define a função | nome_funcao(parametro/argumentos)
def conversao(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
    #retorno da função ao ser chamada
    
print(conversao(212)) 
#exibe o retorno da função com os parametros '212'   

#versão recebendo o dado

temperatura = float(input("Informe a temperatura em Fahrenheit: "))

def conversao_com_input():
    return (temperatura - 32) * 5 / 9

print(conversao_com_input())

