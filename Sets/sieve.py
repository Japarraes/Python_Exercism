def primes(limit):
    
    # Total numbers in range
    numbers = set(range(2, limit+1))

    # Composite numbers in range
    # composite = []
    # for n in numbers:
    #     for m in range(2*n, limit+1, n):
    #         composite.append(m)

    #     composite = list(set(composite))
    composite = {m for n in numbers for m in range(2*n, limit+1, n)}

    # return sorted(numbers - sert(composite))
    return sorted(numbers - composite)





print(primes(10))    # [2, 3, 5, 7]
