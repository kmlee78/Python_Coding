# 단어장을 만들고 그 단어들로 퀴즈를 만들어 맞추는 프로그램
from random import randint

# 새로운 단어장 파일 vocabulary.txt를 만들어 준다
in_file = open('vocabulary.txt', 'w')

# 계속해서 단어들을 입력. q를 누르면 입력을 끝낼 수 있다
while True:
    eng = input("영어단어 입력: ")
    if eng == 'q':
        break
    kor = input("한국어 뜻 입력: ")
    if kor == 'q':
        break
    in_file.write("%s: %s\n" % (kor, eng))

in_file.close()


# 새롭게 만들어진 vocabulary.txt파일을 연다
in_file = open('vocabulary.txt', 'r')
word_dict = {}
size = 0
for value in in_file:
    size += 1
    word_dict[size] = value

# 만들어진 단어장 안에서 랜덤으로 단어를 뽑아 뜻을 맞추는 퀴즈. q를 입력하면 종료
while True:
    word = word_dict[randint(1, size)]
    word = word.strip().split(": ")
    answer = input("%s: " % word[1])
    if answer == word[0]:
        print("맞았습니다!\n")
    elif answer == "q":
        break
    else:
        print("아쉽습니다. 정답은 %s입니다.\n" % word[0])

in_file.close()