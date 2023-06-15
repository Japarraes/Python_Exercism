def translate(text):
    VOWELS = {"a", "e", "i", "o", "u"}
    CLUSTERS_2 = {"ch", "th", "qu", "rh"}
    CLUSTERS_3 = {"sch", "squ", "thr"}
    SPECIALS = {"xr", "yt"}

    piggy = []
    for word in text.split():
        if word[0] in VOWELS or word[:2] in SPECIALS:
            piggy.append(word + "ay")
            continue
        if word[:3] in CLUSTERS_3:
            piggy.append(word[3:] + word[:3] + "ay")
            continue
        if word[:2] in CLUSTERS_2:
            piggy.append(word[2:] + word[:2] + "ay")
            continue
        if word[0] not in VOWELS and (word[1] in VOWELS or word[1] == "y"):
            piggy.append(word[1:] + word[0] + "ay")

    return " ".join(piggy)

print(translate("quick fast run"))
