DECIMALS = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
ROMANS = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")

def roman(number):

    roman_num = ""
    while number > 0:
        for num in DECIMALS:
            div = number // num
            number = number % num
            roman_num += div*(ROMANS[DECIMALS.index(num)])

    return roman_num

print(roman(1))        # "I"
print(roman(2))        # "II"
print(roman(3))        # "III"
print(roman(4))        # "IV"
print(roman(5))        # "V"
print(roman(6))        # "VI"
print(roman(9))        # "IX"
print(roman(16))       # "XVI"
print(roman(27))       # "XXVII"
print(roman(48))       # "XLVIII"
print(roman(49))       # "XLIX"
print(roman(59))       # "LIX"
print(roman(66))       # "LXVI"
print(roman(93))       # "XCIII"
print(roman(141))      # "CXLI"
print(roman(163))      # "CLXIII"
print(roman(166))      # "CLXVI"
print(roman(402))      # "CDII"
print(roman(575))      # "DLXXV"
print(roman(666))      # "DCLXVI"
print(roman(911))      # "CMXI"
print(roman(1024))     # "MXXIV"
print(roman(1666))     # "MDCLXVI"
print(roman(3000))     # "MMM"
print(roman(3001))     # "MMMI"
print(roman(3999))     # "MMMCMXCIX"