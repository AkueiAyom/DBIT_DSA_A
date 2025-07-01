def find_min(lst):
    if len(lst) == 0:
        return None
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value