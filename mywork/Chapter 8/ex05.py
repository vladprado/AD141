from sys import argv, exit

if len(argv) > 2:
    file1 = argv[1]
    file2 = argv[2]
else:
    file1 = input("Digite o nome do arquivo de entrada: ")
    file2 = input("Digite o nome do arquivo de saída: ")

try:
    f1 = open(file1, "r")
    f2 = open(file2, "w")
except OSError as err:
    print("ERRO: " + str(err))
    exit("Falha ao abrir arquivo de entrada.")

while True:
    linha = f1.readline()
    if linha:
        f2.write(linha)
    else:
        break
f1.close()
f2.close()
