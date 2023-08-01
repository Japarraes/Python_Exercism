from string import ascii_uppercase

ALPHABET = list(ascii_uppercase)

def rows(letter):

    result = []
    index = ALPHABET.index(letter)
    for i in range(index+1):
        
        line = [" "]*(index*2+1)
        pos = index - i
        line[pos] = ALPHABET[i]
        pos = index + i
        line[pos] = ALPHABET[i]
        
        result.append("".join(line))

    return result[:-1] + result[::-1]

print(rows("D"))
