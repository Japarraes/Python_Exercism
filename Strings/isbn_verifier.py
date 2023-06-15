def is_valid(isbn):
    
    isbn = isbn.replace("-","")

    if not len(isbn) == 10:
        return False
    
    sum = 0
    for i in range(0, len(isbn)):
        if isbn[i].isdigit():
            sum += int(isbn[i]) * (len(isbn) - i)
        else:
            if i == (len(isbn)-1) and (isbn[len(isbn)-1].upper() == "X"):
                sum += 10
            else:
                return False

    if sum % 11 == 0:
        return True
    else:
        return False
    
print(is_valid("3-598-21508-8"))  # True
print(is_valid("3-598-21508-9"))  # False
print(is_valid("3-598-21507-X"))  # True
print(is_valid("3-598-21507-A"))  # False
print(is_valid("3-598-P1581-X"))  # False
print(is_valid("3598215088"))  # True
