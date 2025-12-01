""" O Método __init__()
Todas as classes possuem um método embutido chamado __init__(), que é sempre executado quando a classe está sendo iniciada.

O método __init__() é usado para atribuir valores às propriedades do objeto ou para realizar operações necessárias quando o objeto está sendo criado. """

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
        
aluno01 = Pessoa("Laura", 20)

print("Nome:", aluno01.nome)        
print("Idade:", aluno01.idade)        

""" Sem o método __init__() , você precisaria definir propriedades manualmente para cada objeto"""