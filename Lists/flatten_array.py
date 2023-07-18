def flatten(iterable):
    
    output = []
    for item in iterable:
        if type(item) == list or type(item) == tuple:
            output.extend(flatten(item))
        else:
            if item != None:
                output.append(item)
        
    return output



print(flatten([]))                                                         # []
print(flatten([0, 1, 2]))                                                  # [0, 1, 2]
print(flatten([[[]]]))                                                     # []
print(flatten([1, [2, 3, 4, 5, 6, 7], 8]))                                 # [1, 2, 3, 4, 5, 6, 7, 8]
print(flatten([0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]))                  # [0, 2, 2, 3, 8, 100, 4, 50, -2]
print(flatten([1, [2, [[3]], [4, [[5]]], 6, 7], 8]))                       # [1, 2, 3, 4, 5, 6, 7, 8]
print(flatten([1, 2, None]))                                               # [1, 2]
print(flatten([None, None, 3]))                                            # [3]
print(flatten([1, None, None, 4]))                                         # [1, 4]
print(flatten([0, 2, [[2, 3], 8, [[100]], None, [[None]]], -2]))           # [0, 2, 2, 3, 8, 100, -2]
print(flatten([None, [[[None]]], None, None, [[None, None], None], None])) # []