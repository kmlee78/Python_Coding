# Linear Search
def linear_search(element, some_list):
    for x in range(len(some_list)):
        if some_list[x] == element:
            return x
    return None

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))


# Binary Search
def binary_search(element, some_list):
    start = 0
    end = len(some_list)-1
    while start <= end:
        middle = (start + end) // 2
        if some_list[middle] == element:
            return middle
        elif some_list[middle] < element:
            start = middle + 1
        else:
            end = middle - 1
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))