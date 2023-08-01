ONES = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six',
    'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
    'thirteen', 'fourteen', 'fifteen', 'sixteen',
    'seventeen', 'eighteen', 'ninteen',
    ]
TENS = [
    '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
    'seventy', 'eighty', 'ninety',
    ]
BASES = (
    (1e9, 'billion'),
    (1e6, 'million'),
    (1e3, 'thousand'),
    (1e2, 'hundred'),
    )

def read_base(num, text):

    text_num = []
    if num > 99:
        num_base = int(num // 100)
        num = int(num % 100)
        if num == 0:
            text_num(f"{ONES[num_base]} {BASES[3][1]} {text}")
        else:
            text_num.append(f"{ONES[num_base]} {BASES[3][1]}")
    if 99 > num > 20:
        num_base = int(num // 10)
        num = int(num % 10)
        if num == 0:
            text_num.append(f"{TENS[num_base]} {text}")
        else:
            text_num.append(f"{TENS[num_base]}-")
    if 20 > num > 0:
        text_num.append(f"{ONES[num]} {text}")

    return text_num

def say(number):
    
    # if the number is negative or is larger than 999,999,999,999 --> Error("input out of range")
    if not 0 <= number < 1e12:
        raise ValueError('input out of range')
    
    if number == 0:
        return ONES[number]
    
    temp = []
    for base, numText in BASES:
        if number >= base:
            # Get number of billion, million, thousand or hundred
            num_base = int(number // base)
            temp.append(tuple([num_base, numText]))
            number = int(number % base)
    
    result = []
    
    for item in temp:
        result += read_base(item[0], item[1])
            
    if number >= 20:
        num_base = int(number // 10)
        number = int(number % 10)
        if number == 0:
            result.append(f"{TENS[num_base]}")
        else:
            result.append(f"{TENS[num_base]}-")

    if 0 < number < 20:
        result.append(ONES[number])
    
    return " ".join(result).replace("- ", "-")



print(say(1234567890))    
# nine hundred eighty-seven billion six hundred fifty-four million three hundred twenty-one thousand one hundred twenty-three