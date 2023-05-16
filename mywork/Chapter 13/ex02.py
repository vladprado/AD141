import random

selected_number = random.randint(1, 100)

print("Estou pensando em um número de 1 a 100")
guess = input("Tente advinhar meu número: ")

tentativas_ok = 0
tentativas_invalidas = 0

while True:
    if not guess.isnumeric() or int(guess) < 0 or int(guess) > 100:
        guess = input("Não é uma tentativa válida. Tente de novo: ")
        tentativas_invalidas += 1
    elif int(guess) > selected_number:
        guess = input("{} está acima. Tente de novo: ".format(int(guess)))
        tentativas_ok += 1
    elif int(guess) < selected_number:
        guess = input("{} está abaixo. Tente de novo: ".format(int(guess)))
        tentativas_ok += 1
    else:
        break

print("{} está correto. Você tentou advinhar o número {} vezes e fez {} tentativas inválidas.".format(guess, tentativas_ok, tentativas_invalidas))
