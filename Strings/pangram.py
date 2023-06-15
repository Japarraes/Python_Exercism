def is_pangram(sentence):
    
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    sentence = sentence.lower()
    for letter in alphabet:
        if not letter in sentence:
            return False
    
    return True

print(is_pangram(""))
print(is_pangram("abcdefghijklMnopqrstuvwxyz"))
print(is_pangram("the quick brown fox jumps over the lazy dog"))
print(is_pangram("a quick movement of the enemy will jeopardize five gunboats"))
