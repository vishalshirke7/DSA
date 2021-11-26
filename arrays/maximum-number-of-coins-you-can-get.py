"""
https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
"""


#own accepted
def maxCoins(piles):
	number_of_piles, max_coin = len(piles) // 3, 0
	piles.sort()
	for index in range(len(piles) - 2, 0, -2):
		# print(piles[index])
		if number_of_piles == 0:
			break
		max_coin += piles[index]
		number_of_piles -= 1
	return max_coin

"""
public int maxCoins(int[] A) {
        Arrays.sort(A);
        int res = 0, n = A.length;
        for (int i = n / 3; i < n; i += 2)
            res += A[i];
        return res;
    }
"""

print('Output', maxCoins([2, 4, 5]))
print('Output', maxCoins([2,4,1,2,7,8]))
print('Output', maxCoins([9,8,7,6,5,1,2,3,4]))
