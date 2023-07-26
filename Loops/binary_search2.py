def find(search_list, value):
    
    return binary_search(sorted(search_list), 0, len(search_list)-1, value)


def binary_search(list, start, end, value):

    # Binary_search using recursive method
    if end < start:
        raise ValueError("value not in array")

    mid = (start + end) // 2

    if list[mid] == value:
        return mid
    elif list[mid] > value:
        return binary_search(list, start, mid-1, value)
    elif list[mid] < value:
        return binary_search(list, mid+1, end, value)


print(find([6], 6))                                                     # 0
print(find([1, 3, 4, 6, 8, 9, 11], 6))                                  # 3
print(find([1, 3, 4, 6, 8, 9, 11], 1))                                  # 0
print(find([1, 3, 4, 6, 8, 9, 11], 11))                                 # 6
print(find([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 634], 144))  # 9
print(find([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], 21))        # 5
print(find([1, 3, 4, 6, 8, 9, 11], 7))                                  # "value not in array"
print(find([1, 3, 4, 6, 8, 9, 11], 0))                                  # "value not in array"
print(find([], 1))                                                      # "value not in array"
print(find([1, 2], 0))                                                  # "value not in array"