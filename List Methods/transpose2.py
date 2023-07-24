def transpose(lines):

    lines = lines.split("\n")
    max_leght = max([len(item) for item in lines])

    lines = map(lambda row: row.ljust(max_leght, "*"), lines)
    lines = map(lambda row: "".join(list(row)), zip(*lines))
    lines = map(lambda row: row.replace("*", " "), lines)

    return "\n".join(lines)


# lines = []  # []
# lines = ["A1"] # ["A", "1"]
# lines = ["A", "1"] # ["A1"]
# lines = ["ABC", "123"] # ["A1", "B2", "C3"]
# lines = ["Single line."]   # ["S", "i", "n", "g", "l", "e", " ", "l", "i", "n", "e", "."]
# lines = ["The fourth line.", "The fifth line."]    # ["TT", "hh", "ee", "  ", "ff", "oi", "uf", "rt", "th", "h ", " l", "li", "in", "ne", "e.", "."]
# lines = ["The first line.", "The second line."]    # ["TT", "hh", "ee", "  ", "fs", "ie", "rc", "so", "tn", " d", "l ", "il", "ni", "en", ".e", " ."]
# lines = ["The longest line.", "A long line.", "A longer line.", "A line."] # ["TAAA", "h   ", "elll", " ooi", "lnnn", "ogge", "n e.", "glr", "ei ", "snl", "tei", " .n", "l e", "i .", "n", "e", "."]
# lines = ["HEART", "EMBER", "ABUSE", "RESIN", "TREND"]  # ["HEART", "EMBER", "ABUSE", "RESIN", "TREND"]
# lines = ["FRACTURE", "OUTLINED", "BLOOMING", "SEPTETTE"]   # ["FOBS", "RULE", "ATOP", "CLOT", "TIME", "UNIT", "RENT", "EDGE"]
lines = ["T", "EE", "AAA", "SSSS", "EEEEE", "RRRRRR"]  # ["TEASER", " EASER", "  ASER", "   SER", "    ER", "     R"]
# lines = ["11", "2", "3333", "444", "555555", "66666"]  # ["123456", "1 3456", "  3456", "  3 56", "    56", "    5"]

print(transpose("\n".join(lines)))