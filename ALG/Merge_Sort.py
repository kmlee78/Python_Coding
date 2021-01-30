# 두 배열을 받아 하나의 정렬된 배열로 합쳐 리턴하는 함수
def merge(list1, list2):
    new_list = []
    index_1 = 0
    index_2 = 0
    while index_1 < len(list1) and index_2 < len(list2):
        if list1[index_1] >= list2[index_2]:
            new_list.append(list2[index_2])
            index_2 += 1
        else:
            new_list.append(list1[index_1])
            index_1 += 1

    if index_1 == len(list1):
        new_list += list2[index_2:]
    elif index_2 == len(list2):
        new_list += list1[index_1:]
    return new_list

# 합병 정렬
def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list
    middle = len(my_list) // 2
    return merge(merge_sort(my_list[:middle]), merge_sort(my_list[middle:]))

print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))