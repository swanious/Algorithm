def solution(triangle):
    n = len(triangle)
    for i in range(1, n):
        for j in range(i + 1):
            # 맨 왼쪽의 값
            if j==0:
                triangle[i][j] += triangle[i-1][j]
            # 맨 오른쪽의 값
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            # 중간의 값들은 이전 행의 두개의 값 중 큰 값을 저장
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
            
    return max(triangle[-1])