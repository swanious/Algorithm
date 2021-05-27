def hex_to_dec(num16):
    value = 0

    for i in range(len(num16)):
        if '0' <= num16[i] <= '9':
            tmp = ord(num16[i]) - ord('0')
        else:
            tmp = ord(num16[i]) - ord('A') + 10
        value += tmp * (16 ** (L - 1 - i))
    return value


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    L = N // 4  # N은 4의 배수이므로 하나의 비밀번호 길이는 L(회전)

    password = list(input())

    ans = set()  # 중복된 값을 넣지 않게

    for i in range(L):
        # 0번부터 L번 스텝을 뛰면서 사용
        for j in range(0, N, L):
            # L의 길이만큼 잘라서 16진수 형태로 넣는다.
            ans.add("".join(password[j:j + L]))
            
            # 내장함수 사용법
            #ans.add(int("".join(password[j:j+L], 16))
            
        password.insert(0, password.pop())
    ans = list(ans)
    ans.sort(reverse=True)

    print("#{} {}".format(tc, hex_to_dec(ans[K-1])))


################################################################

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    L = N // 4  # N은 4의 배수이므로 하나의 비밀번호 길이는 L(회전)

    password = input()

    ans = set()  # 중복된 값을 넣지 않게

    # L만큼 회전시키면 처음과 덧붙이는 값이 동일하므로, L-1까지 회전시킨 값을 더해준다.
    password += password[:L-1]

    for i in range(N):
        ans.add(int(password[i:i+L], 16))

    ans = list(ans)
    ans.sort(reverse=True)
    print("#{} {}".format(tc, ans[K-1]))