from string import ascii_lowercase, ascii_uppercase

def rotate(text, key):
    
    alphabet = str.maketrans(ascii_lowercase + ascii_uppercase,
                        ascii_lowercase[key:] + ascii_lowercase[:key] +
                        ascii_uppercase[key:] + ascii_uppercase[:key])
    
    #return str.translate(text, alphabet)
    return text.translate(alphabet)


#print(rotate("a", 0))   # a
#print(rotate("a", 1))   # b
#print(rotate("a", 26))  # a
#print(rotate("m", 13))  # z
#print(rotate("OMG", 5))  # TRL
#print(rotate("O M G", 5))  # T R L
print(rotate("Testing 1 2 3 testing", 4))  # Xiwxmrk 1 2 3 xiwxmrk
