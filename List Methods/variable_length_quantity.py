def encode(numbers):#
    res = []
    # for i in numbers:
    #     res += encode_one(i)

    for num in numbers:
        # Convert to binary and remove prefix
        bin_num = bin(num)[2:]
        
        # strip every 7 bits from right most bit
        bin_encoded = []
        num_byte = bin_num[-7:]         # Select the las 7 bit
        remain_bytes = bin_num[:-7]    # Save the rest of bytes
        bin_encoded += ['0' + num_byte] # Complete de byte number
        
        # Do the same before with the number of rest bytes
        while remain_bytes != '':
            num_byte = remain_bytes[-7:].rjust(7, '0')  # Select the las 7 bits and complete with 0 right-justified
            remain_bytes = remain_bytes[:-7]        # Save the resto of bytes
            bin_encoded += ['1' + num_byte]
        
        # Convert from bytes
        for item in reversed(bin_encoded):
            res.append(int(item, 2))

    return res

def decode(bytes_):
    
    res = ''
    decoded_num = []

    for num in bytes_:
        bin_num = bin(num)[2:].rjust(8, '0') # Convert to bytes and 0 right-justified
        
        res += bin_num[1:]     # Save byte number
        
        end = False
        if (bin_num[0] == '0'):
            end = True    # Check if is the final byte number
            decoded_num.append(int(res, 2))
            res = ''
    
    if not end:
        raise ValueError('incomplete sequence')
    
    return decoded_num


# print(encode([0x0]))                 # [0x0]
# print(encode([0x40]))                # [0x40]
# print(encode([0x7F]))                # [0x7F]
# print(encode([0x80]))                # [0x81, 0x0]
# print(encode([0x2000]))              # [0xC0, 0x0]
# print(encode([0x3FFF]))              # [0xFF, 0x7F]
# print(encode([0x4000]))              # [0x81, 0x80, 0x0]
# print(encode([0x100000]))            # [0xC0, 0x80, 0x0]
# print(encode([0x1FFFFF]))            # [0xFF, 0xFF, 0x7F]
# print(encode([0x200000]))            # [0x81, 0x80, 0x80, 0x0]
# print(encode([0x8000000]))           # [0xC0, 0x80, 0x80, 0x0]
# print(encode([0xFFFFFFF]))           # [0xFF, 0xFF, 0xFF, 0x7F]
# print(encode([0x10000000]))          # [0x81, 0x80, 0x80, 0x80, 0x0]
# print(encode([0xFF000000]))          # [0x8F, 0xF8, 0x80, 0x80, 0x0]
# print(encode([0xFFFFFFFF]))          # [0x8F, 0xFF, 0xFF, 0xFF, 0x7F]
# print(encode([0x40, 0x7F]))          # [0x40, 0x7F]
# print(encode([0x4000, 0x123456]))    # [0x81, 0x80, 0x0, 0xC8, 0xE8, 0x56]

# print(decode([0x7F]))                            # [0x7F]
# print(decode([0xC0, 0x0]))                       # [0x2000]
print(decode([0xFF, 0xFF, 0x7F]))                # [0x1FFFFF]
# print(decode([0x81, 0x80, 0x80, 0x0]))           # [0x200000]
# print(decode([0x8F, 0xFF, 0xFF, 0xFF, 0x7F]))    # [0xFFFFFFFF]
# print(decode([0xFF]))                            # "incomplete sequence"
# print(decode([0x80]))                            # "incomplete sequence"