"""
https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
"""

# Recursive -

def isSubsetSum(arr, n, target):

    if (target == 0):
        return True
    if (n == 0):
        return False

    if (arr[n - 1] > target):
        return isSubsetSum(arr, n - 1, target)

    return isSubsetSum(arr, n-1, target) or isSubsetSum(arr, n-1, target- arr[n-1])


# Bottom Up
class Solution:
    def isSubsetSum (self, N, arr, sum):
        cache = [[False for j in range(sum + 1)] for i in range(N + 1)]
        for col in range(sum + 1):
            cache[0][col] = False
        for row in range(N + 1):
            cache[row][0] = True
            
        def backtrack(n, targ, cache):
            if targ == 0:
                return True
            if n == 0:
                return False
            return backtrack(n - 1, targ - arr[n], cache) or backtrack(n - 1, targ, cache)            
        return backtrack(N - 1, sum, cache)    


# O(sum*N)
# Top Down
class Solution:
    def isSubsetSum (self, N, arr, sum):
        def backtrack(n, targ, cache):
            if targ == 0:
                return 1
            if n == 0:
                return 0
            if cache[n - 1][targ] != -1:
                return cache[n - 1][targ]
            if arr[n - 1] > targ:
                cache[n - 1][targ] = backtrack(n - 1, targ, cache)
            else:
                cache[n - 1][targ] = max(backtrack(n - 1, targ - arr[n - 1], cache), backtrack(n - 1, targ, cache))
            return cache[n - 1][targ] 

            
        cache = [[-1 for j in range(sum + 1)] for i in range(N + 1)]
        return backtrack(N, sum, cache)