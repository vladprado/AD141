prompt = "Digite um número (ou a palavra 'fim' para sair): "

numeros = []
total = 0
while True:
    data = input(prompt)
    if data == "fim":
        break

    if not data.isnumeric:
        print("Dado não é número")
        break

    total += int(data)
    numeros.append(int(data))

print("Lista: " + str(numeros))
print("Soma total: " + str(total))
