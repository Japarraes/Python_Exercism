ANIMALS = ("fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse")
PHRASES = (
                "I don't know why she swallowed the fly. Perhaps she'll die.",
                "It wriggled and jiggled and tickled inside her.",
                "How absurd to swallow a bird!",
                "Imagine that, to swallow a cat!",
                "What a hog, to swallow a dog!",
                "Just opened her throat and swallowed a goat!",
                "I don't know how she swallowed a cow!",
                "She's dead, of course!",
            )

def recite(start_verse, end_verse):

    verses = []
    for number in range(start_verse, end_verse + 1):

        verses.append(f"I know an old lady who swallowed a {ANIMALS[number-1]}.")
        verses.append(PHRASES[number-1])

        if number not in [1, 8]:
            for index in range(number-1, 0, -1):
                verses.append(f"She swallowed the {ANIMALS[index]} to catch the {ANIMALS[index - 1]}"  +
                                f"{' that wriggled and jiggled and tickled inside her' if index == 2 else ''}.")
            
            verses.append(PHRASES[0])

        if number < end_verse:
            verses.append("")
            
    return verses

print(recite(1,3))