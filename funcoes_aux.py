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
        for j in range(i,len(lista)):
            lista[menor].get_data_postagem() > lista[j].get_data_postagem()
            menor = j
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux
    
    return lista
