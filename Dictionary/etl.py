def transform(legacy_data):
    
    # dict_result = {}
    # for key, item in legacy_data.items():
    #     for letter in item:
    #         dict_result[letter.lower()] = key

    # return dict_result

    return {letter.lower(): key for key, item in legacy_data.items() for letter in item }


legacy_data = {
            1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
            2: ["D", "G"],
            3: ["B", "C", "M", "P"],
            4: ["F", "H", "V", "W", "Y"],
            5: ["K"],
            8: ["J", "X"],
            10: ["Q", "Z"],
        }
print(transform(legacy_data))

# data = {
#             "a": 1, "b": 3,  "c": 3, "d": 2, "e": 1,
#             "f": 4, "g": 2,  "h": 4, "i": 1, "j": 8,
#             "k": 5, "l": 1,  "m": 3, "n": 1, "o": 1,
#             "p": 3, "q": 10, "r": 1, "s": 1, "t": 1,
#             "u": 1, "v": 4,  "w": 4, "x": 8, "y": 4,
#             "z": 10,
#         }