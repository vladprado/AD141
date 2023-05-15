from math import factorial

dic_fatoriais = {x: factorial(x) for x in range(1, 11)}

print(dic_fatoriais)

print(dic_fatoriais.get(5) * dic_fatoriais.get(6))
