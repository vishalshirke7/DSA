"""
https://leetcode.com/problems/duplicate-zeros/
"""

# OWN O(n^2)
def duplicateZeros(arr):
    array_size = len(arr)
    index = 0
    while index < array_size:
        if arr[index] == 0:
            for j in range(array_size - 1, index, -1):
                arr[j] = arr[j - 1]
            index += 2
        else:
            index += 1
    print(arr)

def duplicateZeros(arr):
    array_size = len(arr)
    zero_count = 0
    for val in arr:
        if val == 0:
            zero_count += 1
    for index in range(array_size - 1, -1, -1):
        if index + zero_count < array_size:
            arr[index + zero_count] = arr[index]
        if arr[index] == 0:
            zero_count -= 1
            if index + zero_count < array_size:
                arr[index + zero_count] = arr[index]
        print(arr)
    print('Output', arr)

def duplicateZeros(arr):
    array_size = len(arr)
    zero_count = 0
    for val in arr:
        if val == 0:
            zero_count += 1
    print('Output', arr)    


duplicateZeros([1,0,2,3,0,4,5,0])

"""
    
    int n = A.length, count = 0;
    
    for (int num : A) if (num == 0) count++;
    int i = n - 1;
    int write = n + count - 1;
    
    while (i >= 0 && write >= 0)  {
      
      if (A[i] != 0) { // Non-zero, just write it in
        if (write < n) A[write] = A[i];
        
      } else { // Zero found, write it in twice if we can
        if (write < n) A[write] = A[i];
        write--;
        if (write < n) A[write] = A[i];
      }
      
      i--;
      write--;
"""          