"""*args e **kwargs
Por padrão, uma função deve ser chamada com o número correto de argumentos.

No entanto, às vezes você pode não saber quantos argumentos serão aplicados à sua função.

*args e **kwargs permitem que funções aceitem um número desconhecido de argumentos."""

""" Se você não souber quantos argumentos serão passados para sua função, adicione um a antes do nome do parâmetro.*
 
Dessa forma, a função receberá uma tupla de argumentos e poderá acessar os itens de acordo:"""

def nome_criancas(*criancas): #não se sabe quantos argumentos serão recebidos
    print("A criança mais nova é:", criancas[2]) #exibe somente o argumento que estiver no indice 2 
    
nome_criancas("João", "Maria", "José", "Matheus") #passa diversos argumentos (somente o de indice 2 será exibido no return da função)   
