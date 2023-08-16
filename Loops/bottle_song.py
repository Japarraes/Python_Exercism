BOTTLE_SONG = [ "$ green bottles hanging on the wall,",
                "And if one green bottle should accidentally fall,",
                "There'll be & green bottles hanging on the wall."]
NUMBERS = {
    0: "no",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10:  "Ten",
}

def recite(start, take=1):
    
    result  = []
    for i in range(1, take+1):
        
        if i != 1:
            result.append("")

        for index, line in enumerate(BOTTLE_SONG):
            
            if index == 0:
                if start == 1:
                    line = line.replace("bottles", "bottle")
                result.append(line.replace("$", NUMBERS.get(start)))
                result.append(line.replace("$", NUMBERS.get(start)))
            elif index == len(BOTTLE_SONG)-1:
                start -= 1
                if start == 1:
                    line = line.replace("bottles", "bottle")
                result.append(line.replace("&", NUMBERS.get(start).lower()))
            else:
                result.append(line)

    return result



print(recite(start=2))              # expected = [
                                #     "One green bottle hanging on the wall,",
                                #     "One green bottle hanging on the wall,",
                                #     "And if one green bottle should accidentally fall,",
                                #     "There'll be no green bottles hanging on the wall.",
                                # ]
# print(recite(start=2))              # expected = [
#                             #           "Two green bottles hanging on the wall,",
#                             #           "Two green bottles hanging on the wall,",
#                             #           "And if one green bottle should accidentally fall,",
#                             #           "There'll be one green bottle hanging on the wall.",
#                             #           ]

# print(recite(start=10, take=2))   # expected = [
                            #           "Ten green bottles hanging on the wall,",
                            #           "Ten green bottles hanging on the wall,",
                            #           "And if one green bottle should accidentally fall,",
                            #           "There'll be nine green bottles hanging on the wall.",
                            #           "",
                            #           "Nine green bottles hanging on the wall,",
                            #           "Nine green bottles hanging on the wall,",
                            #           "And if one green bottle should accidentally fall,",
                            #           "There'll be eight green bottles hanging on the wall.",
                            #           ]