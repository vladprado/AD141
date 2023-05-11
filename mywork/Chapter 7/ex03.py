import signal

total = 0

while True:
    try:
        num = input("Digite um número ou Ctrl + D para sair: ")
        total += int(num)
    except ValueError:
        print("Digite números válidos")        
    except KeyboardInterrupt:
        print("\nUse Ctrl + D para sair.")
    except EOFError:
        break

print("\nTotal: ", total)