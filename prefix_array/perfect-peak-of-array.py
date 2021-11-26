"""
https://www.interviewbit.com/problems/perfect-peak-of-array/
"""



def perfectPeak(A):
	left, right = 0, len(A) - 1
	for index in range(1, len(A) - 1):
	    not_special = False
		while left < index < right:
			if A[left] < A[index] < A[right]:
				left += 1
				right -= 1
			else:
			    not_special = True
				break
		if not not_special:
    		while left < index:
    			if A[index] > A[left]:
    				left += 1
    			else:
    				break
    		while right > index:
    			if A[index] < A[right]:
    				right -= 1
    			else:
    				break
    		if left == index == right:
    			return 1
		right = len(A) - 1
	return 0

def findElement(arr):  
    n=len(arr)
    # leftMax[i] stores maximum of arr[0..i-1]  
    leftMax = [None] * n  
    leftMax[0] = float('-inf')  
  
    # Fill leftMax[]1..n-1]  
    for i in range(1, n):  
        leftMax[i] = max(leftMax[i-1], arr[i-1])  
  
    # Initialize minimum from right  
    rightMin = float('inf')  
  
    # Traverse array from right  
    for i in range(n-1, -1, -1):  
       
        # Check if we found a required element  
        if leftMax[i] < arr[i] and rightMin > arr[i]:  
            return 1
  
        # Update right minimum  
        rightMin = min(rightMin, arr[i])  
       
    # If there was no element matching criteria  
    return 0 

print(perfectPeak([5, 1, 4, 3, 6, 8, 10, 7, 9]))	
# print(perfectPeak([1, 5]))