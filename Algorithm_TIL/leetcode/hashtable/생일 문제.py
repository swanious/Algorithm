# 2명이 똑같은 생일일 확률이 23명이면 50%에 육박하고, 57명이 모이면 99%를 넘어선다는 문제

import random

TRIALS = 100000
same_birthdays = 0

for _ in range(TRIALS):
    birthdays = []
    # 23명이 모였을때, 생일이 같을 경우 same_birthdays + 1
    for i in range(23):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            same_birthdays += 1
            break
        birthdays.append(birthday)

print(same_birthdays / TRIALS * 100)

# 실험 결과 23명일때 50% +- 1%정도, 57명일 때 99% +- 1%정도로 실험 완료
