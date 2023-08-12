def sum_of_multiples(limit, multiples):
    
    
    # Check multiples is not empty
    if not multiples:
        return 0
    
    # Calculate multiples of level(limit) for every value(multiples)
    # list_multiples = []
    # for value in multiples:
    #     # Check ZeroDivisionError
    #     if value == 0:
    #         continue

    #     level = limit-1
    #     while value <= level < limit:
    #         if level % value == 0:
    #             list_multiples.append(level)
    #         level -= 1
    list_multiples = [i for i in range(min(multiples), limit) if any(i % factor == 0 for factor in multiples if factor != 0)]
    
    # Sum all values no duplicates
    return sum(set(list_multiples))



# print(sum_of_multiples(1, [3, 5]))                  # 0
# print(sum_of_multiples(4, [3, 5]))                  # 3
# print(sum_of_multiples(7, [3]))                     # 9
# print(sum_of_multiples(10, [3, 5]))                 # 23
# print(sum_of_multiples(100, [3, 5]))                # 2318
# print(sum_of_multiples(1000, [3, 5]))               # 233168
# print(sum_of_multiples(20, [7, 13, 17]))            # 51
# print(sum_of_multiples(15, [4, 6]))                 # 30
# print(sum_of_multiples(150, [5, 6, 8]))             # 4419
# print(sum_of_multiples(51, [5, 25]))                # 275
# print(sum_of_multiples(10000, [43, 47]))            # 2203160
# print(sum_of_multiples(100, [1]))                   # 4950
# print(sum_of_multiples(10000, []))                  # 0
print(sum_of_multiples(1, [0]))                     # 0
# print(sum_of_multiples(4, [3, 0]))                  # 3
# print(sum_of_multiples(10000, [2, 3, 5, 7, 11]))    # 39614537