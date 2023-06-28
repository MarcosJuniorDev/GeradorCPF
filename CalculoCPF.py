import random


try:
    cpf_sem_ponto = ""
    for i in range(9):
        cpf_sem_ponto += str(random.randint(0,9))
    
    
    cpf = cpf_sem_ponto
    lista = []

    for num in cpf:
        lista.append(num)

    resultado = 0
    contador = 10
    while contador >= 2:
        for item in lista:
            resultado1 = int(item) * contador
            resultado += resultado1
            contador -= 1
        resultado *= 10

    cpf_resultado1 = resultado % 11

    if cpf_resultado1 > 9:
        cpf_resultado1 = 0
    
    resultado = 0
    contador = 11
    lista.append(cpf_resultado1)



    while contador >= 2:
        for item in lista:
            resultado1 = int(item) * contador
            resultado += resultado1
            contador -= 1
        resultado *= 10

    cpf_resultado2 = resultado % 11

    if cpf_resultado2 > 9:
        cpf_resultado2 = 0

    cpf_total = str(cpf_resultado1) + str(cpf_resultado2)

    cpf_final = ""
    for item in cpf_sem_ponto:
        cpf_final += str(item)

    cpf_sem_ponto += cpf_total
    print(cpf_sem_ponto)

except:
    print("Dado invalido")


