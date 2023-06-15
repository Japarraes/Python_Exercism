from string import ascii_lowercase
from string import ascii_uppercase

def rotate(text, key):
    
    alphabet_lower = list(ascii_lowercase)
    alphabet_upper = list(ascii_uppercase)
    text_list = list(text)
    rotate_text = ""

    for letter in text_list:
        if letter.isupper():
            alphabet = alphabet_upper
        elif letter.islower():
            alphabet = alphabet_lower
        else:
            rotate_text += letter
            continue

        index = alphabet.index(letter) + key
        if index >= 26:
            index -= 26
        rotate_text += alphabet[index]

    return rotate_text


#print(rotate("a", 0))   # a
#print(rotate("a", 1))   # b
#print(rotate("a", 26))  # a
#print(rotate("m", 13))  # z
#print(rotate("OMG", 5))  # TRL
#print(rotate("O M G", 5))  # T R L
print(rotate("Testing 1 2 3 testing", 4))  # Xiwxmrk 1 2 3 xiwxmrk
