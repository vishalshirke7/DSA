"""
https://leetcode.com/problems/count-number-of-nice-subarrays/
"""

def numberOfSubarrays(nums, k):
	start = end = odd_count = answer = 0
	while end < len(nums):
		if nums[end] % 2 == 1:
			odd_count += 1
		while start < end and odd_count > k:
			if nums[start] % 2 == 1:
				odd_count -= 1
			start += 1
		if odd_count == k:
			answer += 1
		temp_start = start
		while odd_count == k and temp_start < end and nums[temp_start] % 2 == 0:
			answer += 1
			temp_start += 1
		end += 1
	return answer


def numberOfSubarrays(nums, k):
	cur_ptr = count = output = 0
	for index in range(len(nums)):
		if nums[index] & 1:
			k -= 1
			count = 0
		while k == 0:
			k += nums[cur_ptr] & 1
			count += 1
			cur_ptr += 1
		output += count
	return output

print('Output', numberOfSubarrays([1,1,2,1,1], 3))
print('Output', numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))
	

# because for K =1 , [2,2,1] is a valid list, so does, [2,1] and [1].

def numberOfSubarrays(nums, k):
	dic = { 0: 1 }
	cnt = res = 0
	for idx, num in enumerate(nums):
		if num % 2 == 1:
			cnt += 1

		if cnt - k in dic:
			res += dic[cnt-k]

		dic[cnt] = dic.get(cnt, 0) + 1

	return res

"""
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        unordered_map<int, int> m;
        const int n = nums.size();
        int rst = 0;
        int acc = 0;
        m[0] = 1;
        for (int i = 0; i < n; ++i) {
            acc += (nums[i]%2);
            rst += m[acc-k];
            m[acc]++;
        }
        return rst;
    }
};
"""
