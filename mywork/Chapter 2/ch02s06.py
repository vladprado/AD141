inicio = int(input("Digite o menor valor: "))
fim = int(input("Digite o maior valor: "))
step = int(input("Digite o intervalor: "))

if step > 0 and inicio > fim:
    print("Não comnsigo incrementar de maior para menor.")
elif step < 0 and fim > inicio:
    print("Não consigo decrementar de menor para maior.")
elif step == 0:
    print("Intervalo 0 não movimenta")
else:
    for num in range(inicio, fim + int((step / abs(step))), step):
        print(num)
