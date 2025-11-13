# match combinando valores nos cases
#usa-se o | para checar mais de um valor por vez. Exemplo:

dia = 2

match dia:
    case 2 | 3 | 4 | 5 | 6:
        print("Estamos durante a semana")
    case 7 | 1:
        print("Estamos no final de semana")