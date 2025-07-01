def linear_search(list, target):
    for index in range(len(list)):
        if list[index] == target:
            return index
    return -1