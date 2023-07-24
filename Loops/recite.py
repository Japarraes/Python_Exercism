TEXT = [
        'the house that Jack built.',
        'the malt that lay in ',
        'the rat that ate ',
        'the cat that killed ',
        'the dog that worried ',
        'the cow with the crumpled horn that tossed ',
        'the maiden all forlorn that milked ',
        'the man all tattered and torn that kissed ',
        'the priest all shaven and shorn that married ',
        'the rooster that crowed in the morn that woke ',
        'the farmer sowing his corn that kept ',
        'the horse and the hound and the horn that belonged to '
    ]

# def verse(n):
#     # return 'This is ' + ''.join([PARTS[i] for i in range(n - 1, -1, -1)])
#     text = "This is "
#     print(range(n-1, -1, -1))
#     for i in range(n-1, -1, -1):
#         text += PARTS[i]
    
#     return text


def recite(start_verse, end_verse):
    # return [verse(i) for i in range(start_verse, end_verse + 1)]
    verse_list = []
    
    for i in range(start_verse, (end_verse + 1)):
        
        verse = "This is "
        
        for j in range(i-1, -1, -1):
            verse += TEXT[j]
        verse_list.append(verse)

    return verse_list


# print(recite(1, 1))     # ["This is the house that Jack built."])
# print(recite(2, 2))     # ["This is the malt that lay in the house that Jack built."])
# print(recite(3, 3))     # ["This is the rat that ate the malt that lay in the house that Jack built."])
# print(recite(4, 4))     # ["This is the cat that killed the rat that ate the malt that lay in the house that Jack built."])
# print(recite(5, 5))     # ["This is the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."])
# print(recite(6, 6))     # ["This is the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."])
# print(recite(8, 8))     # ["This is the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."])
# print(recite(9, 9))     # ["This is the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."])
# print(recite(10, 10))   # ["This is the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."])
# print(recite(11, 11))   # ["This is the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."])
# print(recite(12, 12))   # ["This is the horse and the hound and the horn that belonged to the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."])
print(recite(4, 8))     # ["This is the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                        #  "This is the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                        #  "This is the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."
                        #  "This is the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."
                        #  "This is the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."])
# print(recite(1, 12))    # ["This is the house that Jack built.",
#                         #  "This is the malt that lay in the house that Jack built.",
#                         #  "This is the rat that ate the malt that lay in the house that Jack built.",
#                         #  "This is the cat that killed the rat that ate the malt that lay in the house that Jack built.",
#                         #  "This is the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
#                         #  "This is the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
#                         #  "This is the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
#                         #  "This is the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
#                         #  "This is the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
#                         #  "This is the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
#                         #  "This is the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
#                         #  "This is the horse and the hound and the horn that belonged to the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."])