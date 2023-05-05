list = input("Digite uma lista de números: ")

for num in list.split():
    if not num.isnumeric():
        continue

    if int(num) > 0:
        print(num)
