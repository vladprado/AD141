def eh_maior(*valores, num):
    quantidade = 0
    for item in valores:

        if item > num:
            quantidade += 1
    
    return quantidade
    

valores = (1, 10, 40, 5, -5, -98, 7, -62)

print(eh_maior(1, 10, 40, 5, -5, -98, 7, -62, num=2))
