def findLength(nums1, nums2):
    nums1_max_subarray = maxSubarray(nums1, nums2, isFirstArray=True)
    nums2_max_subarray = maxSubarray(nums1, nums2, isFirstArray=False)
    print(nums1_max_subarray, nums2_max_subarray)
    return max(nums1_max_subarray, nums2_max_subarray)

def maxSubarray(nums1, nums2, isFirstArray):
    ptr1, ptr2, maxsub, cur = 0, 0, 0, 0
    if isFirstArray:
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] == nums2[ptr2]:
                cur += 1
                ptr1 += 1
                ptr2 += 1
            else:
                ptr2 += 1
                maxsub = max(cur, maxsub)
                cur = 0
    else:
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            print(nums2[ptr2], nums1[ptr1])
            if nums1[ptr1] == nums2[ptr2]:
                cur += 1
                ptr1 += 1
                ptr2 += 1
            else:
                ptr1 += 1
                print('cur, maxsub', cur, maxsub)
                maxsub = max(cur, maxsub)
                cur = 0
    maxsub = max(cur, maxsub)
    return maxsub


print(findLength([5,14,53,80,48], [50,47,3,80,83]))


"""101107419030"""