import json

frequencia = {}
mais_frequente = ""
maior_contagem = 0
with open("cyclone", "r") as f:
    for linha in f:
        for palavra in linha.split():
            if frequencia.get(palavra):
                frequencia[palavra] += 1
            else:
                frequencia[palavra] = 1
            if frequencia[palavra] > maior_contagem:
                mais_frequente = palavra
                maior_contagem = frequencia[palavra]

with open("frequencia.json", "w") as freq:
    json.dump(frequencia, freq, indent="\t")

print("A palavra mais frequente foi {} com {} repetições.".
      format(mais_frequente, maior_contagem))
