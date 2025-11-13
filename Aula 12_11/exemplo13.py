# match combinando valores com if

mes = 2
dia = 6

match dia:
    # dia {numero} se mes igual a {numero}
    case 2 | 3 | 4 | 5 | 6 if mes == 1:
        print("Estamos durante uma semana em janeiro")
    case 2 | 3 | 4 | 5 | 6 if mes == 2:
        print("Estamos durante uma semana em fevereiro")
    case _:
        print("Mês indefinido")
    