"""
수업의 시작 시간과 끝 시간이 튜플로 저장되어 있는 배열이
주어졌을 때 서로 겹치지 않고 최대한 많은 수업을 들을 수 있는
방법을 배열로 리턴하는 함수
"""

def course_selection(course_list):
    new_list = []
    # 튜플의 두번째 값 기준으로 정렬: 일찍 끝나는 수업 순으로 정렬
    course_list = sorted(course_list, key=lambda course: course[1])
    new_list.append(course_list[0])
    for index in range(1, len(course_list)):
        if course_list[index][0] > new_list[-1][1]:
            new_list.append(course_list[index])
    return new_list

print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
