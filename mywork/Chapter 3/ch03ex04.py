prompt = "Digite uma frase (ou a palavra 'fim' para sair): "

palavras = set()
while True:
    data = input(prompt)
    if data == "fim":
        break

    palavras.add(data)

print("Lista: " + str(sorted(palavras)))
print("Unicas: " + str(len(palavras)))
