def annotate(minefield):
    # Function body starts here
    matrix = []

    if not minefield:
        return []
    
    # Convert list<str> to matrix<array>
    for line in minefield:
        matrix.append(list(line))
    
    # Check the board receives malformed input
    if any(len(line) != len(matrix[0]) for line in matrix):
        raise ValueError("The board is invalid with current input.")
    
    len_row = len(matrix)
    len_column = len(matrix[0])
    for row in range(len_row):
        for column in range(len_column):
            # Check if value in matrix is " " or "*"
            if matrix[row][column] not in " *":
                raise ValueError("The board is invalid with current input.")
            
            if matrix[row][column] == "*":
                continue

            # Check adjacents with "*"
            count_mine = 0

            if (column + 1) < len_column and matrix[row][column+1] == "*":
                count_mine += 1
            if (column - 1) >= 0 and matrix[row][column-1] == "*":
                count_mine += 1
            if (row + 1) < len_row:
                if matrix[row+1][column] == "*":
                    count_mine += 1
                if (column + 1) < len_column and matrix[row+1][column+1] == "*":
                    count_mine += 1
                if (column - 1) >= 0 and matrix[row+1][column-1] == "*":
                    count_mine += 1
            if (row - 1) >= 0:
                if matrix[row-1][column] == "*":
                    count_mine += 1
                if (column + 1) < len_column and matrix[row-1][column+1] == "*":
                    count_mine += 1
                if (column - 1) >= 0 and matrix[row-1][column-1] == "*":
                    count_mine += 1
            
            if count_mine > 0:
                matrix[row][column] = str(count_mine)

    return ["".join(line) for line in matrix]

# print(annotate([]))                                                             # []
# print(annotate([""]))                                                           # [""]
# print(annotate(["   ", "   ", "   "]))                                          # ["   ", "   ", "   "]
# print(annotate(["***", "***", "***"]))                                          # ["***", "***", "***"]
# print(annotate(["   ", " * ", "   "]))                                          # ["111", "1*1", "111"]
# print(annotate(["***", "* *", "***"]))                                          # ["***", "*8*", "***"]
# print(annotate([" * * "]))                                                      # ["1*2*1"]
# print(annotate(["*   *"]))                                                      # ["*1 1*"]
# print(annotate([" ", "*", " ", "*", " "]))                                      # ["1", "*", "2", "*", "1"]
# print(annotate(["*", " ", " ", " ", "*"]))                                      # ["*", "1", " ", "1", "*"]
# print(annotate(["  *  ", "  *  ", "*****", "  *  ", "  *  "]))                  # [" 2*2 ", "25*52", "*****", "25*52", " 2*2 "],)
# print(annotate([" *  * ", "  *   ", "    * ", "   * *", " *  * ", "      "]))   # ["1*22*1", "12*322", " 123*2", "112*4*", "1*22*2", "111111"]
print(annotate([" ", "*  ", "  "]) )                                            # "The board is invalid with current input."
print(annotate(["X  * "]))                                                      # "The board is invalid with current input."
