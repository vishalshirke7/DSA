"""
https://www.interviewbit.com/problems/distribute-candy/

"""

def candy(A):
    n = len(A)
    arr = [1 for i in range(n)]
    for i in range(1, n):
        if A[i] > A[i-1]:
            arr[i] = arr[i-1] + 1
    for i in range(n-2, -1, -1):
        if A[i] > A[i+1] and arr[i] <= arr[i+1]:
            arr[i] = arr[i+1] + 1     
    return sum(arr)

def candy(A):
    l=[1]*len(A)
    for x in range(len(A)-1):
        if A[x]<A[x+1]:
            l[x+1]=l[x]+1
    for x in range(len(A)-2,-1,-1):
        if A[x]>A[x+1] and l[x]<=l[x+1]:
            l[x]=l[x+1]+1
    return sum(l)    

# need to correct
def candy(A):
	min_candies, array_length = 0, len(A)
	for index in range():
		pass
	print(min_candies)


candy([1, 2])