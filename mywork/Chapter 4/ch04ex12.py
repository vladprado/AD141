def adiciona_dic(dicionario, valor):
    for chave in dicionario.keys():
        dicionario[chave] += valor
    return dicionario


dados = {
    "Joao": 1,
    "Paulo": 2,
    "Marcos": 0,
    "Mateus": 10
}

print(adiciona_dic(dados, 15))