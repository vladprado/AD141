def eh_positivo(num):
    if num > 0:
        return True
    else: 
        return False

numeros = [-1, 7, 4, -34, 45, 76, -50, -98]

nova_lista = list(filter(eh_positivo, numeros))

print(nova_lista)
