def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    peg_list = [1,2,3]
    new_peg = 0
    for x in peg_list:
        if x != start_peg and x != end_peg:
            new_peg = x

    if num_disks > 1:
        hanoi(num_disks-1, start_peg, new_peg)

    move_disk(num_disks, start_peg, end_peg)

    if num_disks > 1:
        hanoi(num_disks-1, new_peg, end_peg)

# 테스트
hanoi(3, 1, 3)