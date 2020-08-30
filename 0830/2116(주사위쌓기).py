N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
dice = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}
copy_arr = arr[:]
for i in range(6):
    tmp = [1, 2, 3, 4, 5, 6]
    tmp.remove()