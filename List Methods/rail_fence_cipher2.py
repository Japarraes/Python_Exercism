import math

def waves_positions(rails, len_m):
    # r = list(range(rails))
    # indexes = r + r[1:-1][::-1]
    # return indexes * (len_m // len(indexes) + 1)
    down = list(range(rails))
    up = down[1:-1][::-1]
    waves = math.ceil(len_m / ((rails * 2) - 2))
    
    return (down + up) * waves

def matrix_positions(msg_len, positions):
    matrix_positions = []
    for i in range(msg_len):
        matrix_positions.append((positions[i], i))
    
    # return sorted(matrix_positions)
    return matrix_positions

def encode(message, rails):
    positions = waves_positions(rails, len(message))
    
    # cip_rails = [((positions[i], i), message[i]) for i in range(len(message))]
    rails_encode = matrix_positions(len(message), positions)
    cip_rails = zip(rails_encode, message)
    cip_rails = sorted(cip_rails, key=lambda x: x[0])

    return ''.join([item[1] for item in cip_rails])

def decode(encoded_message, rails):
    positions = waves_positions(rails, len(encoded_message))

    # _rails_decode = sorted([(positions[i], i) for i in range(len(encoded_message))])
    rails_decode = sorted(matrix_positions(len(encoded_message), positions))
    cip_rails = zip(rails_decode, encoded_message)

    cip_rails = sorted(cip_rails, key=lambda x: x[0][1])

    return ''.join([c[1] for c in cip_rails])


# print(encode("XOXOXOXOXOXOXOXOXO", 2))                                           # "XXXXXXXXXOOOOOOOOO"
# print(encode("WEAREDISCOVEREDFLEEATONCE", 3))                                    # "WECRLTEERDSOEEFEAOCAIVDEN"
# print(encode("EXERCISES", 4))                                                    # "ESXIEECSR"
print(decode("ESXIEECSR", 4))                                                    # "EXERCISES"
# print(decode("TEITELHDVLSNHDTISEIIEA", 3))                                       # "THEDEVILISINTHEDETAILS"
# print(decode("EIEXMSMESAORIWSCE", 5))                                            # "EXERCISMISAWESOME"
# print(decode("133714114238148966225439541018335470986172518171757571896261", 6)) #"112358132134558914423337761098715972584418167651094617711286"