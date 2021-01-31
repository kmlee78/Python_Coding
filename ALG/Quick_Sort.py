# 두 요소의 위치를 바꿔주는 함수
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    
"""
pivot을 기준으로 작은 값은 왼쪽으로, 큰 값은 오른쪽으로
배치 후 pivot이 있는 위치의 인덱스값을 리턴
"""
def partition(my_list, start, end):
    i = start
    b = start
    pivot = end
    while i < pivot:
        if my_list[i] <= my_list[pivot]:
            swap_elements(my_list, b, i)
            b += 1
        i += 1
    swap_elements(my_list, b, pivot)
    pivot = b
    return pivot
    
def quicksort(my_list, start=0, end=None):
    if end is None:
        end = len(my_list)-1
    if end - start < 1:
         return
    # pivot 왼쪽 부분과 pivot 오른쪽 부분을 각각 quicksort 함수로 정렬
    pivot = partition(my_list, start, end)
    quicksort(my_list, start, pivot-1)
    quicksort(my_list, pivot+1, end)


list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3) # start, end 파라미터 없이 호출
print(list3)