from string import ascii_lowercase

def is_pangram(sentence):

    alphabet = set(ascii_lowercase)
    return alphabet.issubset(sentence.lower())    


print(is_pangram(""))
print(is_pangram("abcdefghijklMnopqrstuvwxyz"))
print(is_pangram("the quick brown fox jumps over the lazy dog"))
print(is_pangram("a quick movement of the enemy will jeopardize five gunboats"))
