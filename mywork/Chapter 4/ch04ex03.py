def soma(*numeros):
    total = 0
    for num in numeros:
        total += num

    return total


print(soma(1, 2, 3, 4, 5, 6))
