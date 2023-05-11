numeros = {0: "zero",
           1: "um",
           2: "dois",
           3: "tres",
           4: "quatro",
           5: "cinco",
           6: "seis",
           7: "sete",
           8: "oito",
           9: "nove"}

num = input("Digite um número: ")

for chave in num:
    print(numeros[int(chave)], end=" ")

print()
