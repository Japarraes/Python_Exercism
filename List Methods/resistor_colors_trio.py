def label(colors):
    
    band_colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    output = []
    for index in range(3):
        if index != 2:
            output.append(band_colors.index(colors[index].lower()))
        else:
            zeros = band_colors.index(colors[index].lower())
            for zero in range(zeros):
                output.append(0) 
    
    number = int("".join(map(str, output)))

    if (number//10**9) > 1:
        return str(number//10**9) + " gigaohms"
    if (number//10**6) > 1:
        return str(number//10**6) + " megaohms"
    if (number//10**3) > 1:
        return str(number//10**3) + " kiloohms"
    else:
        return str(number) + " ohms"
    
    
print(label(["orange", "orange", "black"]))         # "33 ohms"
print(label(["blue", "grey", "brown"]))             # "680 ohms"
print(label(["red", "black", "red"]))               # "2 kiloohms"
print(label(["green", "brown", "orange"]))          # "51 kiloohms"
print(label(["yellow", "violet", "yellow"]))        # "470 kiloohms"
print(label(["blue", "violet", "blue"]))            # "67 megaohms"
print(label(["black", "black", "black"]))           # "0 ohms"
print(label(["white", "white", "white"]))           # "99 gigaohms"
print(label(["black", "grey", "black"]))            # "8 ohms"
print(label(["blue", "green", "yellow", "orange"])) # "650 kiloohms"