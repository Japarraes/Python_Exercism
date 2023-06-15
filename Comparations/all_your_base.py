def rebase(input_base, digits, output_base):
    
    if input_base < 2:
        raise ValueError('input base must be >= 2')

    if digits:
        if min(digits) < 0 or max(digits) >= input_base:
            raise ValueError('all digits must satisfy 0 <= d < input base')
    else:
        return [0]
    
    if output_base < 2:
        raise ValueError('output base must be >= 2')
    
    # digits.reverse()
    # sum2 = 0
    # for i in range(len(digits)):
    #     sum2 += digits[i]*(input_base**i)
    # La lógica anterior se resume en esta línea:
    n = sum(d*(input_base**i) for i,d in enumerate(digits[::-1]))

    digits_out = []
    while (n > 0):
        digits_out.append(n%output_base)
        n //= output_base
    
    return digits_out[::-1] if digits_out else [0]



#print(rebase(1, [0], 10)) # 'input base must be >= 2'
#print(rebase(2, [1, -1, 1, 0, 1, 0], 10)) # 'all digits must satisfy 0 <= d < input base'
#print(rebase(2, [1, 0, 1, 0, 1, 0], 1)) # 'output base must be >= 2'
#print(rebase(2, [1], 10)) # [1]
#print(rebase(2, [1, 0, 1], 10)) # [5]
#print(rebase(10, [5], 2)) # [1, 0, 1]
print(rebase(rebase(10, [0], 2))) # [0]