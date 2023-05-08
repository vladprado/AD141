def comum(lista1, lista2):
    s1 = set(lista1)
    s2 = set(lista2)

    return list(s1 & s2)


val1 = [1, 2, "carro", "teste"]
val2 = [1, 3, 4, "aviao", "teste"]

val3 = comum(val1, val2)

print("Resultado: ", val3)
