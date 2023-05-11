for num in range(0, 50, 1):
    if num < 10:
        print(end=" ")

    if num % 10 == 9:
        print(num)
    else:
        print(num, end=" ")
