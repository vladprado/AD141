prompt = "Digite uma frase (ou a palavra 'fim' para sair): "

palavras = dict()

while True:
    data = input(prompt)
    if data == "fim":
        break

    valor = palavras.get(data, 0)
    valor += 1
    palavras[data] = valor

palavras_usadas = sorted(palavras.keys())
print("Ordenadas alfabeticamente:")

for palavra in palavras_usadas:
    print(palavra, "foi usada", palavras[palavra], "vezes")

print(palavras)


def sort_por_freq(key):
    return palavras[key]


palavras_usadas.sort(key=sort_por_freq, reverse=True)
print("Ordernadas por frequencia:")
for palavra in palavras_usadas:
    print(palavra, "foi usada", palavras[palavra], "vezes")
