"""
https://www.interviewbit.com/old/problems/max-distance/
"""

def maximumGap(A):
    if len(A)<=1:
        return 0
    A_sorted = sorted(reversed([(ind,i) for ind,i in enumerate(A)]), key=lambda x:x[1], reverse=True)
    overall_max=-float("inf")
    max_index_so_far=-float("inf") 
    for index, value in enumerate(A_sorted):
        max_index_so_far = max(max_index_so_far, value[0])
        overall_max = max(overall_max, max_index_so_far - value[0])
    return overall_max
    

def maximumGap(A):
    array = list(range(len(A)))
    array.sort(key = lambda i:A [i])
    maxDistance = 0
    minSofar = array[0]
    for i in array:
        if i <= minSofar:
            minSofar = i
        else:
            maxDistance = max(maxDistance,i - minSofar)
    return maxDistance

def maximumGap(A):
    A = [(index, val) for index, val in enumerate(A)]
    A = sorted(A, key=lambda x:x[1])
    max_dis = 0
    prefix = [0] * len(A)
    prefix[len(A) - 1] = A[-1][0]
    for index in range(len(A) - 2, -1, -1):
        prefix[index] = max(prefix[index + 1], A[index][0])
    print(A, prefix)
    for index in range(len(A)):
        if prefix[index] != A[index][0]:
            max_dis = max(max_dis, prefix[index] - A[index][0])
    return max_dis


print('Output', maximumGap([3, 5, 4, 2]))