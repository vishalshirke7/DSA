"""
https://leetcode.com/problems/max-consecutive-ones-iii/
https://practice.geeksforgeeks.org/problems/maximize-number-of-1s0905/1
https://www.interviewbit.com/problems/maximum-ones-after-modification/
"""

def findZeroes(arr, n, m) :
    indexes_0 = list()
    for index in range(n):
        if arr[index] == 0:
            indexes_0.append(index)
            
    def get_start(ptr_0):
        if indexes_0[ptr_0 + 1] - indexes_0[ptr_0] > 1:
            return indexes_0[ptr_0] + 1
        return indexes_0[ptr_0 + 1]

    ptr_0 = start = end = count_0 = ans = 0
    while start <= end and end <= n - 1:
        if arr[end] == 0:
            if count_0 == m:
                start = get_start(ptr_0)
                ptr_0 += 1
            else:
                count_0 += 1
        ans = max(ans, end-start+1)
        end += 1
    return ans

print(findZeroes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 19, 3))
print(findZeroes([1,0,0,1,1,0,1,0,1,1,1], 11, 2))
print(findZeroes([1,1,1,0,0,0,1,1,1,1,0], 11, 2))

# 1
def findZeroes(arr, n, m):
    total_max = 0
    current_max = 0
    temp_m = m
    last_valid = None
    temp_m = -1 if m is 0 else m
    for i in range(n):
        if arr[i] == 1:
            if i - 1 < 0:
                current_max += 1
                last_valid = i
            if i - 1 >= 0:
                if arr[i - 1] == 0:
                    last_valid = i
                    if temp_m < 0:
                        current_max = 0
                else:
                    current_max += 1
        elif arr[i] == 0:
            if temp_m < 0:
                pass
            elif temp_m == 0:
                if last_valid is not None:
                    current_max = i - last_valid + 1
                else:
                     current_max = 1
                temp_m = m - 1                
            else:
                current_max += 1
                temp_m -= 1
        total_max = max(total_max, current_max)
    return total_max


# 2
def findZeroes(arr, n, m) :
    wL = wR = 0
    bestL = bestWindow = 0
    zeroCount = 0
    while wR < n:
        if zeroCount <= m :
            if arr[wR] == 0 :
                zeroCount += 1
            wR += 1
        if zeroCount > m :
            if arr[wL] == 0 :
                zeroCount -= 1
            wL += 1
        if (wR-wL > bestWindow) and (zeroCount<=m) :
            bestWindow = wR - wL
            bestL = wL
    for i in range(0, bestWindow):
        if arr[bestL + i] == 0:
            print(bestL + i)
  
arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1]
m = 2
n = len(arr)
findZeroes(arr, n, m)
  
# 3
def longestOnes(nums, k):
    zero_count, start, output = 0, 0, 0
    for index in range(len(nums)):
        if nums[index] == 0:
            zero_count += 1
        while zero_count > k:
            if nums[start] == 0:
                zero_count -= 1
            start += 1
        output = max(output, index - start + 1)
    return output

# 4
def longestOnes(self, A, K):
    i = 0
    for j in xrange(len(A)):
        K -= 1 - A[j]
        if K < 0:
            K += 1 - A[i]
            i += 1
    return j - i + 1

# 5
"""https://leetcode.com/problems/max-consecutive-ones-iii/discuss/719833/Python3-sliding-window-with-clear-example-explains-why-the-soln-works"""
def longestOnes(self, A: List[int], K: int) -> int:
  left = right = 0
  
  for right in range(len(A)):
    if A[right] == 0:
      K -= 1
    if K < 0:
      if A[left] == 0:
        K += 1
      left += 1
  return right - left + 1


print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))