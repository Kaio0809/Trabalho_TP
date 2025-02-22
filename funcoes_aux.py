# Funções auxiliares usadas nas classes
import datetime

def gerador():
    id = 1
    while True:
        yield id
        id += 1

def ordenar_pela_data(lista):
    for i in range(len(lista)):
        menor = datetime.datetime.now()
        indice = 0
        for j in range(i,len(lista)):
            if menor > lista[j].get_data_postagem():
                menor = lista[j].get_data_postagem()
                indice = j
        aux = lista[i]
        lista[i] = lista[indice]
        lista[indice] = aux
    
    return lista