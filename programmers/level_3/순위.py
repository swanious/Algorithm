def solution(n, results):
    answer = 0
    wl_table = [[0] * (n) for _ in range(n)]
    for r in results:
        wl_table[r[0]-1][r[1]-1] = 1 # 승
        wl_table[r[1]-1][r[0]-1] = -1 # 패
        
    for i in range(n):
        for j in range(n):
            if (wl_table[i][j] == 1): # A에게 패배한 B는 A를 이긴 모두에게 짐
                idxs = []
                for idx in range(n):
                    if wl_table[i][idx] == -1:
                        idxs.append(idx)
                for idx in idxs:
                    wl_table[j][idx] = -1
                    
            elif (wl_table[i][j] == -1): # A를 이긴사람은 A에게 진사람한테 이김
                idxs = []
                for idx in range(n):
                    if wl_table[i][idx] == 1:
                        idxs.append(idx)
                for idx in idxs:
                    wl_table[j][idx] = 1
    
    for row in wl_table:
        if row.count(0) == 1:
            answer += 1
            
    return answer