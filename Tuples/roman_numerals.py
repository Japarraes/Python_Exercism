DECIMALS = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
ROMANS = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")

def roman(number):

    roman_num = ""
    while number > 0:
        if number >= 1000:
            number -= 1000
            roman_num += ROMANS[DECIMALS.index(1000)]
        elif number >= 900:
            number -= 900
            roman_num += ROMANS[DECIMALS.index(900)]
        elif number >= 500:
            number -= 500
            roman_num += ROMANS[DECIMALS.index(500)]
        elif number >= 400:
            number -= 400
            roman_num += ROMANS[DECIMALS.index(400)]
        elif number >= 100:
            number -= 100
            roman_num += ROMANS[DECIMALS.index(100)]
        elif number >= 90:
            number -= 90
            roman_num += ROMANS[DECIMALS.index(90)]
        elif number >= 50:
            number -= 50
            roman_num += ROMANS[DECIMALS.index(50)]
        elif number >= 50:
            number -= 50
            roman_num += ROMANS[DECIMALS.index(50)]
        elif number >= 40:
            number -= 40
            roman_num += ROMANS[DECIMALS.index(40)]
        elif number >= 10:
            number -= 10
            roman_num += ROMANS[DECIMALS.index(10)]
        elif number == 9:
            number -= 9
            roman_num += ROMANS[DECIMALS.index(9)]
        elif number <= 8 and number >= 5:
            number -= 5
            roman_num += ROMANS[DECIMALS.index(5)]
        elif number == 4:
            number -= 4
            roman_num += ROMANS[DECIMALS.index(4)]
        elif number < 4:
            number -= 1
            roman_num += ROMANS[DECIMALS.index(1)]

    return roman_num

# print(roman(1))        # "I"
# print(roman(2))        # "II"
# print(roman(3))        # "III"
# print(roman(4))        # "IV"
# print(roman(5))        # "V"
# print(roman(6))        # "VI"
# print(roman(9))        # "IX"
# print(roman(16))       # "XVI"
# print(roman(27))       # "XXVII"
# print(roman(48))       # "XLVIII"
# print(roman(49))       # "XLIX"
# print(roman(59))       # "LIX"
# print(roman(66))       # "LXVI"
# print(roman(93))       # "XCIII"
# print(roman(141))      # "CXLI"
# print(roman(163))      # "CLXIII"
# print(roman(166))      # "CLXVI"
# print(roman(402))      # "CDII"
# print(roman(575))      # "DLXXV"
# print(roman(666))      # "DCLXVI"
# print(roman(911))      # "CMXI"
# print(roman(1024))     # "MXXIV"
# print(roman(1666))     # "MDCLXVI"
# print(roman(3000))     # "MMM"
# print(roman(3001))     # "MMMI"
print(roman(3999))     # "MMMCMXCIX"