import json

with open("books.json", "r") as f:
    livros = json.load(f)

print("Livros:")
print(livros.keys())

while True:
    titulo = input("Digite um titulo: (ou 'fim' para sair.) ").strip()
    if titulo == "fim":
        break

    info = livros.get(titulo)
    if info:
        print("Livro: {}".format(titulo))
        print(""""
 - autor: {}
 - país: {}
 - lingua: {}
 - paginas: {}
 - ano: {}
""".format(info.get("author"),
           info.get("country"),
           info.get("language"),
           info.get("pages"),
           info.get("year")))
    else:
        print("Não existe esse livro na lista. Tente de novo.")
