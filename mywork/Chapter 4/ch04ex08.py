def externa(num1, num2):
    def interna():
        return num1 + num2
    return interna

fun = externa(3, 4)

print(fun())