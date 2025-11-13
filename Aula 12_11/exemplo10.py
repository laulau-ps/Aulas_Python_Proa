# switch case em python (match)

# usado para substituir muitos if/else

# syntax (variavel com valor já definido):

dia = 3

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-Feira")
    case 3:
        print("Terça-Feira")
    case 4:
        print("Quarta-Feira")
    case 5:
        print("Quinta-Feira")
    case 6:
        print("Sexta-Feira")
    case 7:
        print("Sábado")
    case _: # 'default', ele sempre combina, então deve ser usado ao final do código 
        print("Dia inexistente")
        
        