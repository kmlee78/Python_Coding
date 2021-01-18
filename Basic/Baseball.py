# 랜덤한 정수를 추출할 수 있는 함수 임포트
from random import randint

# 정답을 나타내는 배열을 미리 설정
answer = [10, 10, 10, 10]
i = 0
while i < 4:
    new = randint(0,9)
    # 중복되는 수가 발생하지 않게 수를 선택
    if new not in answer[:i]:
      answer[i] = new
      i += 1

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
print()
ball = 0
strike = 0
count = 0
numbers = [10, 10, 10, 10]

# 최종 정답을 나타내는 4스트라이크가 될 때 까지 수행 반복
while strike != 4:
    ball = 0
    strike = 0
    j = 0
    while j < 4:
        numbers[j] = int(input("%d번째 수를 입력하세요: " % int(j+1)))
        if numbers[j] < 0 or numbers[j] > 9:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
        elif numbers[j] in numbers[:j]:
            print("중복되는 수 입니다. 다시 입력해주세요.")
        else:
            # 만약 정답과 일치하는 수가 있다면
            if numbers[j] in answer:
                # 위치 까지 맞으면 스트라이크 1 증가
                if numbers[j] == answer[j]:
                    strike += 1
                # 그렇지 않다면 볼 1 증가
                else:
                    ball += 1
            j += 1
    print("%dS %dB" % (strike, ball))
    # 총 수행 횟수 카운트
    count += 1
print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % count)