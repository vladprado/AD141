def encontra_objeto(lista, objeto, posicao):
    ocorrencias = 0
    for item in lista:
        if item == objeto:
            ocorrencias += 1
        if ocorrencias == posicao:
            return item

    return ValueError


lista1 = [1, "carro", "teste", 2, 1, "carro", "maria"]

print(encontra_objeto(lista1, "carro", 2))