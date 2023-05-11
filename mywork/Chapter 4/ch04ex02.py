def longest_string(textos):
    maior = 0
    for text in textos:
        if len(text) > maior:
            maior = len(text)

    return maior


string_col = ["teste", "maria clara", "vladimir", "mascavo"]

tamanho = longest_string(string_col)

for texto in string_col:
    if len(texto) < tamanho:
        print(texto.rjust(tamanho))
    else:
        print(texto)
