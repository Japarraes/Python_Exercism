DIGIT_PATTERNS = {
    " _ | ||_|   ": "0",
    "     |  |   ": "1",
    " _  _||_    ": "2",
    " _  _| _|   ": "3",
    "   |_|  |   ": "4",
    " _ |_  _|   ": "5",
    " _ |_ |_|   ": "6",
    " _   |  |   ": "7",
    " _ |_||_|   ": "8",
    " _ |_| _|   ": "9",
}

def convert(input_grid):
    
    r = len(input_grid)     # rows
    c = len(input_grid[0])  # colums
    
    # Check the rows are multiples of 4
    if r % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    
    ocr_matrix = []
    for x in range(0, r, 4):
        
        ocr_num = ""
        for i in range(0, c, 3):
            
            digits = []        
            for j in range(4):
                # Check the colums are multiples of 3
                if len(input_grid[x+j]) % 3 != 0:
                    raise ValueError("Number of input columns is not a multiple of three")
                
                digits.append(input_grid[x+j][i:i+3])

            ocr_num += DIGIT_PATTERNS.get("".join(digits), "?")
        
        ocr_matrix.append(ocr_num)

    return ",".join(ocr_matrix)

# print(convert([" _ ", "| |", "   "]))               # "Number of input lines is not a multiple of four"
# print(convert(["    ", "   |", "   |", "    "]))    # "Number of input columns is not a multiple of three"
# print(convert([" _ ", "| |", "|_|", "   "]))        # "0"
# print(convert(["   ", "  |", "  |", "   "]))        # "1"
# print(convert(["   ", "  _", "  |", "   "]))        # "?"
# print(convert([
#             "       _     _        _  _ ",
#             "  |  || |  || |  |  || || |",
#             "  |  ||_|  ||_|  |  ||_||_|",
#             "                           ",
#         ]))                                         # "110101100"
# print(convert([
#             "       _     _           _ ",
#             "  |  || |  || |     || || |",
#             "  |  | _|  ||_|  |  ||_||_|",
#             "                           ",
#         ]))                                         #"11?10?1?0"
# print(convert([" _ ", " _|", "|_ ", "   "]))        # "2"
# print(convert([" _ ", " _|", " _|", "   "]))        # "3"
# print(convert(["   ", "|_|", "  |", "   "]))        # "4"
# print(convert([" _ ", "|_ ", " _|", "   "]))        # "5"
# print(convert([" _ ", "|_ ", "|_|", "   "]))        # "6"
# print(convert([" _ ", "  |", "  |", "   "]))        # "7"
# print(convert([" _ ", "|_|", "|_|", "   "]))        # "8"
# print(convert([" _ ", "|_|", " _|", "   "]))        # "9"
# print(convert([
#             "    _  _     _  _  _  _  _  _ ",
#             "  | _| _||_||_ |_   ||_||_|| |",
#             "  ||_  _|  | _||_|  ||_| _||_|",
#             "                              ",
#         ]))                                         # "1234567890"
print(convert([
            "    _  _ ",
            "  | _| _|",
            "  ||_  _|",
            "         ",
            "    _  _ ",
            "|_||_ |_ ",
            "  | _||_|",
            "         ",
            " _  _  _ ",
            "  ||_||_|",
            "  ||_| _|",
            "         ",
        ]))                                         # "123,456,789"
