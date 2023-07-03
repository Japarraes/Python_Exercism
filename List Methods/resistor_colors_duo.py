def value(colors):
    band_colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    
    i = band_colors.index(colors[0].lower())
    j = band_colors.index(colors[1].lower())

    return str(i)+str(j)

print(value(["brown", "black"]))
