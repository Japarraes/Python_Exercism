def encode(message, rails):
    
    list = ['' for _ in range(rails)]
    row = 0
    dx = 1
    for char in message:
        list[row] += char
        if row + dx == -1:
            dx = 1
        elif row + dx == rails:
            dx = -1
        row += dx
    return ''.join(list)

def decode(encoded_message, rails):
    previous = ''
    test = encoded_message 
    while True:
        previous = test 
        test = encode(test, rails)
        if test == encoded_message:
            return previous


# print(encode("XOXOXOXOXOXOXOXOXO", 2))                                           # "XXXXXXXXXOOOOOOOOO"
# print(encode("WEAREDISCOVEREDFLEEATONCE", 3))                                    # "WECRLTEERDSOEEFEAOCAIVDEN"
# print(encode("EXERCISES", 4))                                                    # "ESXIEECSR"
print(decode("ESXIEECSR", 4))                                                      # "EXERCISES"
# print(decode("TEITELHDVLSNHDTISEIIEA", 3))                                       # "THEDEVILISINTHEDETAILS"
# print(decode("EIEXMSMESAORIWSCE", 5))                                            # "EXERCISMISAWESOME"
# print(decode("133714114238148966225439541018335470986172518171757571896261", 6)) #"112358132134558914423337761098715972584418167651094617711286"