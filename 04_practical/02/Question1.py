def sum_of_elements(lst):
    total = 0
    for number in lst:
        total += number
    return total

if __name__ == "__main__":
    test_list = [1, 2, 3, 4]
    print("Sum:", sum_of_elements(test_list))