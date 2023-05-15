f = open("dataset", "r")
linhas = f.readlines()
f.close()

dic_computers = {}

for linha in linhas:
    dono, tipo, valor = linha.split()
    equipamento = dic_computers.get(dono)
    if not equipamento:
        equipamento = {}
    equipamento[tipo] = valor

    dic_computers[dono] = equipamento

print(dic_computers)
