file1 = input("Digite o nome do arquivo de entrada: ")
file2 = input("Digite o nome do arquivo de saída: ")

f1 = open(file1, "r")
f2 = open(file2, "w")

while True:
    linha = f1.readline()
    if linha:
        f2.write(linha)
    else:
        break
f1.close()
f2.close()
