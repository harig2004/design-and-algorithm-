def find_min_max(arr):
    if not arr:
        return None, None
    elif len(arr) == 1:
        return arr[0], arr[0]

    mid = len(arr) // 2
    min_left, max_left = find_min_max(arr[:mid])
    min_right, max_right = find_min_max(arr[mid:])

    return min(min_left, min_right), max(max_left, max_right)
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_val, max_val = find_min_max(arr)
print("Minimum value:", min_val)
print("Maximum value:", max_val)
