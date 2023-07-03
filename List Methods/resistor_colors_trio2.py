colors = ("black", "brown", "red", "orange", "yellow",
            "green", "blue", "violet", "grey", "white")

def value(color):
    return colors.index(color)

def label(colors):
        d1, d2, e = [value(colors[i]) for i in range(3)]
        r = (10 * d1 + d2) * 10**e
        if r <= 10**3:
            return f"{r} ohms"
        elif r <= 10**6:
            return f"{r//10**3} kiloohms"
        elif r <= 10**9:
            return f"{r//10**6} megaohms"
        else:
            return f"{r//10**9} gigaohms"
    
    
# print(label(["orange", "orange", "black"]))         # "33 ohms"
# print(label(["blue", "grey", "brown"]))             # "680 ohms"
# print(label(["red", "black", "red"]))               # "2 kiloohms"
# print(label(["green", "brown", "orange"]))          # "51 kiloohms"
# print(label(["yellow", "violet", "yellow"]))        # "470 kiloohms"
# print(label(["blue", "violet", "blue"]))            # "67 megaohms"
# print(label(["black", "black", "black"]))           # "0 ohms"
# print(label(["white", "white", "white"]))           # "99 gigaohms"
# print(label(["black", "grey", "black"]))            # "8 ohms"
print(label(["blue", "green", "yellow", "orange"])) # "650 kiloohms"