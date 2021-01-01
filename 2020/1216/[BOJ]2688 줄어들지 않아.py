dp = [[0] * 66 for _ in range(10)]
# 초기값 설정을 위해 1 저장
dp[9][0] = 1
# 각각의 자리수 길이에 대해
for n in range(1, 66):
    # 맨 앞의 값이 9부터 0까지 올 수 있는 정수의 개수를 구한다.
    for digit in range(9, -1, -1):
        # 미리 구해놓은 앞의 자리수 값을 더하기 위한 변수들 지정
        # 맨 앞의 값이 digit이 오기 위해서는 digit 이상의 정수만 올 수 있다.
        # 따라서 n-1 자리의 값이 digit 이상 9 이하의 값의 누적합이 필요.
        under = 0
        left = dp[digit][n-1]
        if digit < 9:
            under = dp[digit+1][n]
        # n-1 자리의 digit의 값(=left) + n자리의 digit-1의 값(=under) = n자리의 digit값(누적합)
        dp[digit][n] = left + under

for tc in range(int(input())):
    n = int(input())
    print(dp[0][n+1])