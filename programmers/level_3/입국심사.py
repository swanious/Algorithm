def solution(n, times):
    import sys
    answer = sys.maxsize
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2
        hap = 0
        hap += sum(mid // time for time in times)
        if (n > hap):
            left = mid + 1
        else:
            right = mid - 1
            answer = min(answer, mid)

    return answer
