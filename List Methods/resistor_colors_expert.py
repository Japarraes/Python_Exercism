colors = ("black", "brown", "red", "orange", "yellow",
            "green", "blue", "violet", "grey", "white")
tolerance = {
    "grey": " ±0.05%",
    "violet": " ±0.1%",
    "blue": " ±0.25%",
    "green": " ±0.5%",
    "brown": " ±1%",
    "red": " ±2%",
    "gold": " ±5%",
    "silver": " ±10%",
}

def valueColors(color):
    return colors.index(color)

def valueTolerance(color):
    return tolerance.get(color)

def resistor_label(colors):
    params = len(colors)
    if params == 1:
        d1 = valueColors(colors[0])
        d2 = 0
        e = 0
        t = ""
    elif params == 2:
        d1, d2 = [valueColors(colors[i]) for i in range(2)]
        e = 0
        t = ""
    elif params == 3:
        d1, d2 = [valueColors(colors[i]) for i in range(2)]
        e = valueColors(colors[len(colors)-1])
        t = ""
    elif params == 4:
        d1, d2 = [valueColors(colors[i]) for i in range(2)]
        e = valueColors(colors[len(colors)-2])
        t = valueTolerance(colors[len(colors)-1])
    elif params == 5:
        d1, d2, d3 = [valueColors(colors[i]) for i in range(3)]
        e = valueColors(colors[len(colors)-2])
        t = valueTolerance(colors[len(colors)-1])
    
    if params == 5:
        r = (100 * d1 + 10 * d2 + d3) * 10**e
    else:
        r = (10 * d1 + d2) * 10**e

    if r <= 10**3:
        return f"{r} ohms{t}"
    elif r <= 10**6:
        return f"{r//10**3 if r%10**3 == 0 else r/10**3} kiloohms{t}"
    elif r <= 10**9:
        return f"{r//10**6 if r%10**6 == 0 else r/10**6} megaohms{t}"
    else:
        return f"{r//10**9 if r%10**9 == 0 else r/10**9} gigaohms{t}"
    

print(resistor_label(["orange", "orange", "black", "red"]))                 # "33 ohms ±2%"
print(resistor_label(["blue", "grey", "brown", "violet"]))                  # "680 ohms ±0.1%"
print(resistor_label(["red", "black", "red", "green"]))                     # "2 kiloohms ±0.5%"
print(resistor_label(["green", "brown", "orange", "grey"]))                 # "51 kiloohms ±0.05%"
print(resistor_label(["black"]))                                            # "0 ohms"
print(resistor_label(["orange", "orange", "yellow", "black", "brown"]))     # "334 ohms ±1%"
print(resistor_label(["red", "green", "yellow", "yellow", "brown"]))        # "2.54 megaohms ±1%"
print(resistor_label(["blue", "grey", "white", "brown", "brown"]))          # "6.89 kiloohms ±1%"
print(resistor_label(["violet", "orange", "red", "grey"]))                  # "7.3 kiloohms ±0.05%"
print(resistor_label(["brown", "red", "orange", "green", "blue"]))          # "12.3 megaohms ±0.25%"
