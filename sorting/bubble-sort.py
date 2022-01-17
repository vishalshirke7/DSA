def bubble_sort(arr):
    size = len(arr)
    for index_i in range(4):
        swapped = False
        for index_j in range(0, size - index_i - 1):
            if arr[index_j] > arr[index_j + 1]:
                arr[index_j], arr[index_j + 1] = arr[index_j + 1], arr[index_j]
                swapped = True
        if not swapped:
            break
    return arr


arr = [7, 10, 4, 3, 20, 15]
print(bubble_sort(arr)) 