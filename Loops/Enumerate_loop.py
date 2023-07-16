word_list = ["bird", "chicken", "barrel", "apple"]

# *index* and *word* are the loop variables.
# Loop variables can be any valid python name.

for index, word in enumerate(word_list):
    if word.startswith("b"):
        print(f"{word.title()} (at index {index}) starts with a B.")
    else:
        print(f"{word.title()} (at index {index}) doesn't start with a B.")

'Bird (at index 0) starts with a B.'
'Chicken (at index 1) doesn\'t start with a B.'
'Barrel (at index 2) starts with a B.'
'Apple (at index 3) doesn\'t start with a B.'


# The same method can be used as a "lookup" for pairing items between two lists.
# Of course, if the lengths or indexes don't line up, this doesn't work.

word_list = ["cat", "chicken", "barrel", "apple", "spinach"]
category_list = ["mammal", "bird", "thing", "fruit", "vegetable"]

for index, word in enumerate(word_list):
    print(f"{word.title()} is in category: {category_list[index]}.")

'Cat is in category: mammal.'
'Chicken is in category: bird.'
'Barrel is in category: thing.'
'Apple is in category: fruit.'
'Spinach is in category: vegetable.'