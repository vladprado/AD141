numbers = [1, 6, 8, 2, 9, 75, 54, 45, 76, 89]

while True:
    try:
        num = input("Digite um número, ou 'fim' para sair: ")
        if num == "fim":
            break        
        num = int(num)
    except ValueError:
        print("Não é um número válido.")
        continue
    
    try:
        print(numbers[num])
        break
    except IndexError:
        print("A lista é menor.")
