"""
https://www.interviewbit.com/old/problems/hotel-bookings-possible/
https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
"""

#O(n)
def minPlatform(arrival, departure, n):
    platform = [0] * 2631
    requiredPlatform = 1
    
    for i in range(n):
        platform[arrival[i]] += 1
        platform[departure[i] + 1] -= 1

    for i in range(1, 2631):
        platform[i] = platform[i] + platform[i - 1]
        requiredPlatform = max(requiredPlatform,
                            platform[i])
        
    return requiredPlatform

#O(n logn)
def findPlatform(arr, dep, n):
    arr.sort()
    dep.sort()
    plat_needed, result = 1, 1
    i, j = 1, 0
    while (i < n and j < n):
        if (arr[i] <= dep[j]):
            plat_needed += 1
            i += 1
        elif (arr[i] > dep[j]):
            plat_needed -= 1
            j += 1
        if (plat_needed > result):
            result = plat_needed
    return result

# O(n^2)
def minPlatform(arr, dep, n):
    current_platforms = min_platform = 1
    size = len(arr)
    for index_i in range(size):
        for index_j in range(index_i + 1, size):
            if (arr[index_i] >= arr[index_j] and arr[index_i] <= dep[index_j]) or (arr[index_i] <= arr[index_j] and arr[index_j] <= dep[index_j]):
                current_platforms += 1
        min_platform = max(current_platforms, min_platform)
    return min_platform

print("Output", findPlatform([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000], 6))
print('Output', findPlatform([900, 1100, 1235], [1000, 1200, 1240], 3))
print('Output', findPlatform([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000], 6))    