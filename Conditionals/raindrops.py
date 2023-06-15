def convert(number):
    raindrop_sounds = ""
    factor = False
    if number % 3 == 0:
        raindrop_sounds += "Pling"
        factor = True
    if number % 5 == 0:
        raindrop_sounds += "Plang"
        factor = True
    if number % 7 == 0:
        raindrop_sounds += "Plong"
        factor = True

    if not factor:
        return str(number)
    else:    
        return raindrop_sounds

print(convert(15))