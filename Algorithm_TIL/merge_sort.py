def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        merge_lst = []
        l, h = low, high

        while l < mid and h < high:
            if arr[l] < arr[h]:
                merge_lst.append(arr[l])
                l += 1
            else:
                merge_lst.append(arr[h])
                h += 1


        while l < mid:
            merge_lst.append(arr[l])
            l += 1

        while h < high:
            merge_lst.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = merge_lst[i - low]

    return sort(0, len(arr))