def arrange_negative_positive(array):
    for i in range(1, len(array)):
        value = array[i]
        if value >= 0:
            continue
        j = i - 1
        while(j >=0 and array[j] > 0):
            array[j + 1] = array[j] 
            j -= 1
        array[j+1] = value
    print(array)


array = [-9, 10, 67, 9, 1, -7, -2, -1, 12]
arrange_negative_positive(array)