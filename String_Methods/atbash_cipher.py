import string

def encode(plain_text):
    
    # "abcdefghijklmnopqrstuvwxyz1234567890"
    plain = string.ascii_lowercase + string.digits 
    
    # "zyxwvutsrqponmlkjihgfedcba1234567890"
    cipher = "".join(sorted(string.ascii_lowercase, reverse=True)) + string.digits   
    
    # Convert plain text to ciphered text
    encode_text = list(code_method(plain_text, plain, cipher))

    # Group string every 5 letters with spaces
    spaces = int(len(encode_text) / 5)
    for x in range(spaces, 0, -1):
        encode_text.insert((x*5), " ") 
    
    return "".join(encode_text).strip()

def decode(ciphered_text):
    
    # "abcdefghijklmnopqrstuvwxyz1234567890"
    plain = string.ascii_lowercase + string.digits 
    
    # "zyxwvutsrqponmlkjihgfedcba1234567890"
    cipher = "".join(sorted(string.ascii_lowercase, reverse=True)) + string.digits   
    
    # Convert ciphered text to plain text
    return code_method(ciphered_text, cipher, plain)

def code_method(plain_text, from_text, to_text):
    # Remove punctuation and spaces
    plain_text = plain_text.translate(str.maketrans('', '', string.punctuation))
    plain_text = plain_text.replace(" ", "").lower()

    # Create map's rules and convert
    encode_rules = str.maketrans(from_text, to_text)

    # Return string without spaces
    return plain_text.translate(encode_rules)

# print(encode("yes"))                                             # "bvh"
# print(encode("no"))                                              # "ml"
# print(encode("OMG"))                                             # "lnt"
# print(encode("O M G"))                                           # "lnt"
# print(encode("mindblowingly"))                                   # "nrmwy oldrm tob"
# print(encode("Testing,1 2 3, testing."))                         # "gvhgr mt123 gvhgr mt"
# print(encode("Truth is fiction."))                               # "gifgs rhurx grlm"
# print(encode("The quick brown fox jumps over the lazy dog."))    # "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"

print(decode("vcvix rhn"))                                   # "exercism"
print(decode("zmlyh gzxov rhlug vmzhg vkkrm thglm v"))       # "anobstacleisoftenasteppingstone"
print(decode("gvhgr mt123 gvhgr mt"))                        # "testing123testing"   
print(decode("gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"))   # "thequickbrownfoxjumpsoverthelazydog"
print(decode("vc vix    r hn"))                              # "exercism"
print(decode("zmlyhgzxovrhlugvmzhgvkkrmthglmv"))             # "anobstacleisoftenasteppingstone"

