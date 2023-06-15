"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one, list_two):
    
    if list_one == list_two:
        return EQUAL
    
    if not list_two:
        return SUPERLIST
    
    if not list_one:
        return SUBLIST
    
    loop = abs(len(list_one) - len(list_two)) + 1
    if (len(list_two) > len(list_one)):
        for i in range(loop):
            if list_two[i:len(list_one)+i] == list_one:
                return SUBLIST
    else:
        for i in range(loop):
            if list_one[i:len(list_two)+i] == list_two:
                return SUPERLIST

    return UNEQUAL


# print(sublist([], []))          # EQUAL
# print(sublist([], [1, 2, 3]))   # SUBLIST
# print(sublist([1, 2, 3], []))   # SUPERLIST
# print(sublist([1, 2, 3], [1, 2, 3]))    # EQUAL
# print(sublist([1, 2, 3], [2, 3, 4]))    # UNEQUAL
print(sublist([1, 2, 5], [0, 1, 2, 3, 1, 2, 5, 6])) # SUBLIST
print(sublist([0, 1, 2, 3, 4, 5], [0, 1, 2]))    # SUPERLIST