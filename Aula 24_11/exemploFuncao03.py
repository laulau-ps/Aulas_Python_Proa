# teste de codigo repetitivo sem função:
''' define 2 variaveis diferentes para realizar o mesmo cálculo '''

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

# com função:

def conversao_f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 #uma função pra cálculo

print(conversao_f_to_c(77)) #chama a função quantas vezes precisar, mudando apenas o parametro 
print(conversao_f_to_c(95))
print(conversao_f_to_c(50))