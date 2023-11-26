def find_smallest_int(arr):
    min_num = arr[-1]
    for num in arr:
        if num < min_num:
            min_num = num
    return min_num