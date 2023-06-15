def steps(number):

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    cont = 0

    while number > 1:

        cont += 1

        if (number % 2) == 0:
            number //= 2
        else:
            number = (number*3) + 1

    return cont

print(steps(16))