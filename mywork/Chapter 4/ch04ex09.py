def externa():
    return lambda num1, num2: num1 + num2

fun = externa()

print(fun(3, 4))