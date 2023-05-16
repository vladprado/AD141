import re 

while True:
    anumber = input("Digite um número ('fim' para sair): ").strip()
    if anumber == "fim":
        break

    check = re.search(r"^-?\d+\.\d+$", anumber)
    if not check:
        print("Não é um número válido.")
        continue

    if anumber[0] == "-":
        print("Número é negativo.")
    else:
        print("Número é positivo.")