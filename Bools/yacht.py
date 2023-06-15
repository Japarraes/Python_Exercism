# Score categories.
# Change the values as you see fit.
YACHT = lambda x: 50 if len(set(x)) == 1 else 0
ONES = lambda x: sum(i for i in x if i == 1)
TWOS = lambda x: sum(i for i in x if i == 2)
THREES = lambda x: sum(i for i in x if i == 3)
FOURS = lambda x: sum(i for i in x if i == 4)
FIVES = lambda x: sum(i for i in x if i == 5)
SIXES = lambda x: sum(i for i in x if i == 6)
FULL_HOUSE = lambda x: sum(x) if len(set(x)) == 2 and any(x.count(i) == 3 for i in set(x)) else 0
FOUR_OF_A_KIND = lambda x: sum(i * 4 for i in set(x) if x.count(i) > 3)
LITTLE_STRAIGHT = lambda x: 30 if sum(x) == 15 and len(set(x)) == 5 else 0
BIG_STRAIGHT = lambda x: 30 if sum(x) == 20 and len(set(x)) == 5 else 0
CHOICE = lambda x: sum(x)

def score(dice, category):
    return category(dice)

print(score([5, 5, 5, 5, 5], YACHT))
print(score([1, 3, 3, 2, 5], YACHT))
print(score([1, 1, 1, 3, 5], ONES))
print(score([3, 1, 1, 5, 1], ONES))
print(score([4, 3, 6, 5, 5], ONES))
print(score([2, 3, 4, 5, 6], TWOS))
print(score([1, 4, 1, 4, 1], FOURS))
print(score([3, 3, 3, 3, 3], THREES))
print(score([3, 3, 3, 3, 3], FIVES))
print(score([1, 5, 3, 5, 3], FIVES))
print(score([2, 3, 4, 5, 6], SIXES))
print(score([2, 2, 4, 4, 4], FULL_HOUSE))
print(score([5, 3, 3, 5, 3], FULL_HOUSE))
print(score([2, 2, 4, 4, 5], FULL_HOUSE))
print(score([1, 4, 4, 4, 4], FULL_HOUSE))
print(score([2, 2, 2, 2, 2], FULL_HOUSE))
print(score([6, 6, 4, 6, 6], FOUR_OF_A_KIND))
print(score([3, 3, 3, 3, 3], FOUR_OF_A_KIND))
print(score([3, 5, 4, 1, 2], LITTLE_STRAIGHT))
print(score([1, 2, 3, 4, 5], BIG_STRAIGHT))
print(score([1, 1, 2, 3, 4], LITTLE_STRAIGHT))
print(score([1, 2, 3, 4, 6], LITTLE_STRAIGHT))
print(score([1, 1, 3, 4, 5], LITTLE_STRAIGHT))
print(score([4, 6, 2, 5, 3], BIG_STRAIGHT))
print(score([6, 5, 4, 3, 2], LITTLE_STRAIGHT))
print(score([6, 5, 4, 3, 1], BIG_STRAIGHT))
print(score([3, 3, 5, 6, 6], CHOICE))
print(score([2, 2, 2, 2, 2], CHOICE))