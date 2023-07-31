"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    return add_items({}, items)

    return dict_result

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items:
        inventory[item] = inventory.get(item) - 1 if inventory.get(item) > 0 else 0
    
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    if inventory.get(item, 0) != 0:
        inventory.pop(item)

    return inventory


def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    # list_tuples = []
    # for key, value in inventory.items():
    #     list_tuples.append(tuple([key, value])) if value > 0 else None

    # return list_tuples
    
    return [(key, value) for (key, value) in inventory.items() if value > 0] 

# print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))  # {"coal":1, "wood":2, "diamond":3}
# print(decrement_items({"iron": 3, "diamond": 4, "gold": 2}, ["iron", "iron", "diamond", "gold", "gold"]))   # {'iron': 1, 'diamond': 3, 'gold': 0}
# print(decrement_items({"wood": 2, "iron": 3, "diamond": 1}, ["wood", "wood", "wood", "iron", "diamond", "diamond"]))   # {'iron': 1, 'diamond': 3, 'gold': 0}
# print(remove_item({"iron": 1, "diamond": 2, "gold": 1}, "diamond"))   # {"iron": 1, "gold": 1}
# print(remove_item({"iron": 1, "diamond": 2, "gold": 1}, "wood"))   # {"iron": 1, "diamond": 2, "gold": 1}
print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))   # [('coal', 7), ('diamond', 2), ('iron', 7), ('wood', 11)]
