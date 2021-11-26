""""
https://www.geeksforgeeks.org/equilibrium-index-of-an-array/
"""


#own 
#Function to find equilibrium point in the array.
def equilibriumPoint(self,A, N):
    # Your code here
    left_sum, right_sum = 0, sum(A[1:])
    if N == 1:
        return 1
    for index in range(1, N):
        left_sum += A[index - 1]
        right_sum -= A[index]
        if left_sum == right_sum:
            return index + 1
    return -1


#editorial 

def equilibrium(arr):
	left_sum = []
	right_sum = []
	for i in range(len(arr)):
		if(i):
			left_sum.append(left_sum[i-1]+arr[i])
			right_sum.append(right_sum[i-1]+arr[len(arr)-1-i])
		else:
			left_sum.append(arr[i])
			right_sum.append(arr[len(arr)-1])
	for i in range(len(arr)):
		if(left_sum[i] == right_sum[len(arr) - 1 - i ]):
			return(i)
	return -1

arr = [-7, 1, 5, 2, -4, 3, 0]
print('First equilibrium index is ',
	equilibrium(arr))