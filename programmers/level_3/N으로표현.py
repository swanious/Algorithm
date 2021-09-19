def solution(N, number):
    new_set = [set()] * 8
    
    for i in range(8):
        new_set[i].add(int(N * (i + 1)))
        for j in range(0, i):
            for arg1 in new_set[i]:
                for arg2 in new_set[i-j-1]:
                    new_set[i].add(arg1+arg2)
                    new_set[i].add(arg1-arg2)
                    new_set[i].add(arg1*arg2)
                    new_set[i].add(arg1//arg2)
                    
        if number in new_set[i]: return i + 1
    return -1