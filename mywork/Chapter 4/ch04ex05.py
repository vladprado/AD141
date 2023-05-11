def somar():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    return num1 + num2


def subtrair():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    return num1 - num2


def multiplicar():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    return num1 * num2


def dividir():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    return num1 / num2


while True:
    print("Opções da Calculadora:")
    print("     1. Somar")
    print("     2. Subtrair")
    print("     3. Nultiplicar")
    print("     4. Dividir")
    print("     5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        somar()
    elif opcao == "2":
        subtrair()
    elif opcao == "3":
        multiplicar()
    elif opcao == "4":
        dividir()
    elif opcao == "5":
        break
    else:
        print("Opção inválida.")
