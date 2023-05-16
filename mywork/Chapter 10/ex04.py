import re

while True:
    produto = input("Digite um produto: ").strip()
    if produto == "fim":
        break

    regex = r"^(\d{2})([A-Z]{2})\s+([\w\s+])"
    match = re.search(regex, produto)

    if match:
        print("Digitos: {}".format(match.group(1)))
        print("Letras: {}".format(match.group(2)))
        print("Descrição: {}".format(match.group(3)))
    else:
        print("Produto inválido.")