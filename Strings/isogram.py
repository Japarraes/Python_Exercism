def is_isogram(string):
    
    # Erase spaces, hyphens and convert to lower case
    string = "".join(string.split()).replace("-","").lower()
    
    # Create a set from string
    letterSet = {x for x in string}
    
    # Check if the len of set is equal to len of string
    return len(letterSet) == len(string)

print(is_isogram("SIX-year-old"))
print(is_isogram("thumbscrew-jappingly"))
print(is_isogram("Emily Jung Schwartzkopf"))