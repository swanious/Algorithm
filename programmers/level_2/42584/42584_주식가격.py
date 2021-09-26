def solution(prices):
    ans = []
    l = len(prices)
    for i in range(l):
        for j in range(i+1, l):
            if prices[i] > prices[j]:
                break
        ans.append(j - i)

    return ans