num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    menor = num2
    maior = num1
elif num2 > num1:
    menor = num1
    maior = num2
else:
    menor = num1
    maior = num1

total = 0
while menor <= maior:
    total += menor
    menor += 1

print("O valor final é {0}".format(total))
