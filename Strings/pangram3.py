import string

def is_pangram(sentence):

    return all(char in sentence.lower() for char in string.ascii_lowercase)


print(is_pangram(""))
print(is_pangram("abcdefghijklMnopqrstuvwxyz"))
print(is_pangram("the quick brown fox jumps over the lazy dog"))
print(is_pangram("a quick movement of the enemy will jeopardize five gunboats"))
