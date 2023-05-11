def soma(*numeros):
    total = 0
    media = 0
    for num in numeros:
        total += num
    
    media = total / len(numeros)
    return total, media


print(soma(1, 2, 3, 4, 5, 6))
