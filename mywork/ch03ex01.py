first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]

third = []

for item in range(len(first)):
    third.append(first[item] + second[item])

print(third)

teste = first + second

print(teste)
