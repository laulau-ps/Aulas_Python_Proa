#laço for - else com brake

for i in range(6):
    if i == 3: break
    print(i)
else:
    print("Loop finalizado")
    
    #o bloco else não será executado, pois o laço finaliza antes com o brake