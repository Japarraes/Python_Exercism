def find(search_list, value):
    
    start = 0
    end = len(search_list) - 1

    while (end >= start):
        mid = (start + end) // 2

        if search_list[mid] == value:
            return mid
        elif search_list[mid] > value:
            end = mid -1
        elif search_list[mid] < value:
            start = mid + 1

    if end < start:
        raise ValueError("value not in array")
    

# print(find([6], 6))                                                     # 0
# print(find([1, 3, 4, 6, 8, 9, 11], 6))                                  # 3
# print(find([1, 3, 4, 6, 8, 9, 11], 1))                                  # 0
# print(find([1, 3, 4, 6, 8, 9, 11], 11))                                 # 6
# print(find([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 634], 144))  # 9
# print(find([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], 21))        # 5
print(find([1, 3, 4, 6, 8, 9, 11], 7))                                  # "value not in array"
# print(find([1, 3, 4, 6, 8, 9, 11], 0))                                  # "value not in array"
# print(find([], 1))                                                      # "value not in array"
# print(find([1, 2], 0))                                                  # "value not in array"