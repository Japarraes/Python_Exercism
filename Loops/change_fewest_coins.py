
def find_fewest_coins(coins, target):
    
    if target < 0:
        raise ValueError("target can't be negative")
    # The number of coins required to reach a given sub_target.
    count = [target + 1] * (target + 1)
    first_coin = [0] * (target + 1)
    count[0] = 0
    for pos in range(1, target + 1):
        for coin in coins:
            remaining_target = pos - coin
            if remaining_target < 0 or count[pos] <= count[remaining_target] + 1:
                continue
            count[pos] = count[remaining_target] + 1
            first_coin[pos] = coin
    if count[target] > target:
        raise ValueError("can't make target with given coins")
    result = []

    while target != 0:
        result.append(first_coin[target])
        target -= first_coin[target]
    
    return result

# print(find_fewest_coins([1, 5, 10, 25], 1))                  # [1]
# print(find_fewest_coins([1, 5, 10, 25, 100], 25))            # [25]
# print(find_fewest_coins([1, 5, 10, 25, 100], 15))            # [5, 10]
# print(find_fewest_coins([1, 4, 15, 20, 50], 23))             # [4, 4, 15]
# print(find_fewest_coins([1, 5, 10, 21, 25], 63))             # [21, 21, 21]
# print(find_fewest_coins([1, 2, 5, 10, 20, 50, 100], 999))    # [2, 2, 5, 20, 20, 50, 100, 100, 100, 100, 100, 100, 100, 100, 100]
# print(find_fewest_coins([2, 5, 10, 20, 50], 21))             # [2, 2, 2, 5, 10]
print(find_fewest_coins([4, 5], 27))                         # [4, 4, 4, 5, 5, 5]
# print(find_fewest_coins([1, 5, 10, 21, 25], 0))              # []
# print(find_fewest_coins([5, 10], 3))                         # "can't make target with given coins")
# print(find_fewest_coins[5, 10], 94)                          # "can't make target with given coins")
# print(find_fewest_coins([1, 2, 5], -5))                      # "target can't be negative")
