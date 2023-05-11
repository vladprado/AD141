prompt = "Digite um número (ou a palavra 'fim' para sair): "

numeros = set()
duplicados = 0
while True:
    data = input(prompt)
    if data == "fim":
        break

    if not data.isnumeric:
        print("Dado não é número")
        break

    if int(data) in numeros:
        duplicados += 1

    numeros.add(int(data))

print("Lista: " + str(numeros))
print("Duplicados: " + str(duplicados))
