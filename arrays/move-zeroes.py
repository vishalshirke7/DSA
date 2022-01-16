"""
https://leetcode.com/explore/featured/card/fun-with-arrays/511/in-place-operations/3157/
"""

def moveZeroes(nums):
    first_occur = None
    for index in range(len(nums)):
        if nums[index] == 0:
            print('0 value at ', index)
            if first_occur is None:
                first_occur = index
        else:
            if first_occur is not None:
                nums[first_occur], nums[index] = nums[index], nums[first_occur]
                if (index - first_occur) > 1:
                    first_occur += 1
                else:
                    first_occur = index
        print('first_occur', first_occur)
        print(nums)
        

moveZeroes([0,1,0,3,12])

"""

def moveZeroes(self, nums):
        pos = 0
        for i in range(len(nums)):
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
"""                
