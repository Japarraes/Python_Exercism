def saddle_points(matrix):
    
    # Check if input matrix is empty
    if not matrix:
        return matrix

    # Check irregular matrix
    for line in matrix:
        if len(line) != len(matrix[0]):
            raise ValueError("irregular matrix")
        
    # Create transpose matrix
    zip_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    # zip_matrix = []
    # for i in range(len(matrix[0])):
    #     line = []
    #     for j in range(len(matrix)):
    #         line.append(matrix[j][i])
    #     zip_matrix.append(line)

    # Find the max value in matrix-line and the min value in zip_matrix-line
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == max(matrix[i]) and matrix[i][j] == min(zip_matrix[j]):
                result.append({"row": i+1, "column": j+1})
                
    return result


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
