def commands(binary_str):
    
    handshake = []
    reversed = True

    for number in range(len(binary_str)):
        
        match(number):
            case 0:
                if binary_str[number] == "1":
                    reversed = False
                continue
            case 1:
                if binary_str[number] == "1":
                    handshake.append("jump")
                continue
            case 2:
                if binary_str[number] == "1":
                    handshake.append("close your eyes")
                continue
            case 3:
                if binary_str[number] == "1":
                    handshake.append("double blink")
                continue
            case 4:
                if binary_str[number] == "1":
                    handshake.append("wink")
                continue
    
    if reversed:
        handshake = handshake[::-1]

    return handshake

#print(commands("00001"))
#print(commands("00010"))
#print(commands("00100"))
#print(commands("01000"))
print(commands("00011"))
print(commands("10011"))

