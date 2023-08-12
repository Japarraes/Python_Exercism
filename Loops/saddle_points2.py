def saddle_points(matrix):
    
    # Check irregular matrix
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError('irregular matrix')
    
    # Find max value for every row
    row_maxima = list(map(max, matrix))
    
    # Find min value for every column
    col_minima = list(map(min, list(zip(*matrix))))
    
    return [
        {'row': r+1, 'column': c+1}
        for r, row_max in enumerate(row_maxima)
        for c, col_min in enumerate(col_minima)
        if row_max == col_min
    ]


# matrix = [  [9, 8, 7], 
#             [5, 3, 2], 
#             [6, 6, 7]]
# print(saddle_points(matrix))                # [{"row": 2, "column": 1}]

# matrix = []
# print(saddle_points(matrix))                # []

# matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
# print(saddle_points(matrix))                # []

# matrix = [[4, 5, 4], [3, 5, 5], [1, 5, 4]]
# print(saddle_points(matrix))                # [
#                                             #  {"row": 1, "column": 2},
#                                             #  {"row": 2, "column": 2},
#                                             #  {"row": 3, "column": 2},
#                                             # ]

# matrix = [[6, 7, 8], [5, 5, 5], [7, 5, 6]]
# print(saddle_points(matrix))                # [
#                                             #  {"row": 2, "column": 1},
#                                             #  {"row": 2, "column": 2},
#                                             #  {"row": 2, "column": 3},
#                                             # ]

# matrix = [[8, 7, 9], [6, 7, 6], [3, 2, 5]]
# print(saddle_points(matrix))                # [{"row": 3, "column": 3}]

# matrix = [  [3, 1, 3], 
#             [3, 2, 4]]
# print(saddle_points(matrix))                # [
#                                             #  {"row": 1, "column": 3}, 
#                                             #  {"row": 1, "column": 1}
#                                             # ]

# matrix = [[2], [1], [4], [1]]
# print(saddle_points(matrix))                # [
#                                             #  {"row": 2, "column": 1}, 
#                                             #  {"row": 4, "column": 1}
#                                             # ]

# matrix = [[2, 5, 3, 5]]
# print(saddle_points(matrix))                # [
#                                             #  {"row": 1, "column": 2}, 
#                                             #  {"row": 1, "column": 4}
#                                             # ]

matrix = [[3, 2, 1], [0, 1], [2, 1, 0]]
print(saddle_points(matrix))                # "irregular matrix"
