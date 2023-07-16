def is_paired(input_string):
    
    openBrackets = "[{("
    closeBrackets = "]})"
    stackBrackets = []
    
    for bracket in input_string:
        if bracket in openBrackets:
            stackBrackets.append(bracket)
        elif bracket in closeBrackets:
            if not stackBrackets:
                return False
            if openBrackets[closeBrackets.index(bracket)] != stackBrackets.pop():
                return False
                
    return not stackBrackets
    


print(is_paired("[ ["))  # False
print(is_paired("}{"))  # False
print(is_paired("[({}])"))  # False
print(is_paired("([{}({}[])])"))  # True