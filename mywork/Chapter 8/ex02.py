from sys import argv

argv.pop(0)
if argv[0].startswith("-t"):
    exibe_totais = True
    argv.pop(0)
else:
    exibe_totais = False

g_linhas = g_palavras = g_caracteres = 0

for filename in argv:
    f = open(filename, "r")
    linhas = palavras = caracteres = 0
    for linha in f:
        linhas += 1
        caracteres += len(linha)
        palavras += len(linha.split(None))
    f.close()
    g_linhas += linhas
    g_palavras += palavras
    g_caracteres += caracteres
    if not exibe_totais:
        print("{} tem {} linhas, {} caracteres e {} palavras".
              format(filename, linhas, caracteres, palavras))

if exibe_totais:
    print("No total foram {} linhas, {} caracteres e {} palavras".
          format(g_linhas, g_caracteres, g_palavras))
