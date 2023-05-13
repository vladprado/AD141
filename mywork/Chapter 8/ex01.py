from sys import argv

for filename in argv:
    f = open(filename, "r")
    linhas = palavras = caracteres = 0
    for linha in f:
        linhas += 1
        caracteres += len(linha)
        palavras += len(linha.split(None))
    f.close()
    print("{} tem {} linhas, {} caracteres e {} palavras".
          format(filename, linhas, caracteres, palavras))
