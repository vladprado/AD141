from sys import argv, exit

if len(argv) != 3:
    print("Uso: " + argv[0] + " <arquivo1> <arquivo2>")
    exit(1)

try:
    f1 = open(argv[1], "r")
    f2 = open(argv[2], "r")
except OSError as err:
    print("ERRO: " + str(err))

s1 = set()

for linha in f1:
    s1.add(linha.strip())
print(s1)
s2 = set()

for linha in f2:
    s2.add(linha.strip())
print(s2)
s3 = s1 & s2

print(s3)
