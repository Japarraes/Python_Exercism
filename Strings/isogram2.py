def is_isogram(string):
    
    # Create list empty
    letters = []

    # Erase spaces, hyphens and convert to lower case
    string = "".join(string.split()).replace("-","").lower()
    
    # Check is every letter in string is in the list letters.
    for s in string:
        if s in letters:
            return False
        else:
            letters.append(s)
    return True

print(is_isogram("SIX-year-old"))
print(is_isogram("thumbscrew-jappingly"))
print(is_isogram("Emily Jung Schwartzkopf"))