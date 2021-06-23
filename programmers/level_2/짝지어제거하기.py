def solution(s):
    stack = []
    # 문자열의 갯수가 홀수면 볼필요없음
    if len(s) % 2:
        return 0

    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
            continue

        stack.append(s[i])

        # 남은 문자열의 갯수가 stack의 길이보다 크면 볼필요없음
        if len(s) - i < len(stack):
            return 0

    return 1
