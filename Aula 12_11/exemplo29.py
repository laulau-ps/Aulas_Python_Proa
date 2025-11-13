#laço for - pass

""" for loops não podem estar vazios, mas se você algum motivo tem um loop sem conteúdo, coloque pass na instrução for para evitar obter um erro. """

# exemplo melhor:

for numero in [1,2,3,4,5,10]:
    if numero < 3:
        pass # não faz nada, 'ignora' esse pedaço do código e continua o laço
    if numero == 3:
        continue # pula para o próximo número e continua o laço
    if numero == 10:
        break # interrompe o laço inteiro
    print(f"Número final: {numero}")
    
    # este código faz o seguinte: ao iniciar o loop ele passa por 3 validações:
    '''
    1 - esse número é menor que 3? se sim, passa e executa o print ao final
    2 - esse numero é igual a 3? se sim, continua, ou seja, pula o numero 3 e inicia o laço novamente
    3- o numero é igual a 10? se sim, interrompe o laço
    '''