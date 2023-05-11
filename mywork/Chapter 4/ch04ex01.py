def valid_number():
    number = input("Digite um número inteiro positivo: ")

    if not number.isnumeric():
        return 0
    elif int(number) <= 0:
        return 0
    else:
        return int(number)


retorno = valid_number()

if retorno == 0:
    print("Não é um número válido.")
