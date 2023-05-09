text = input("Digite um texto: ")

print(f"Termina com ponto: {text.endswith('.')}")
print(f"Todos os caracteres são alfa: {text.isalpha()}")
print(f"Tem x no texto: {text.find('x') > 0}")

texto_modificado = text.replace('e', 'E')

print(texto_modificado)
