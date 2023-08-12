def sum_of_multiples(limit, multiples):
    
    return sum(
        set(
            num
            for num in range(limit)
            for multiple in multiples
            if (multiple != 0) and (num % multiple == 0)
        )
    )

print(sum_of_multiples(1, [3, 5]))                  # 0
print(sum_of_multiples(4, [3, 5]))                  # 3
print(sum_of_multiples(7, [3]))                     # 9
print(sum_of_multiples(10, [3, 5]))                 # 23
print(sum_of_multiples(100, [3, 5]))                # 2318
print(sum_of_multiples(1000, [3, 5]))               # 233168
print(sum_of_multiples(20, [7, 13, 17]))            # 51
print(sum_of_multiples(15, [4, 6]))                 # 30
print(sum_of_multiples(150, [5, 6, 8]))             # 4419
print(sum_of_multiples(51, [5, 25]))                # 275
print(sum_of_multiples(10000, [43, 47]))            # 2203160
print(sum_of_multiples(100, [1]))                   # 4950
print(sum_of_multiples(10000, []))                  # 0
print(sum_of_multiples(1, [0]))                     # 0
print(sum_of_multiples(4, [3, 0]))                  # 3
print(sum_of_multiples(10000, [2, 3, 5, 7, 11]))    # 39614537