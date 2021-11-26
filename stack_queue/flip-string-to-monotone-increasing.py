"""
https://leetcode.com/problems/flip-string-to-monotone-increasing/
"""
def minFlipsMonoIncr(s):
	zeroes = ones = 0
	for char in s:
		if char == '0':
			zeroes += 1
	min_flips = zeroes
	for char in s:
		ones += char == '1'
		zeroes -= char == '0'
		min_flips = min(min_flips, zeroes + ones)
	return min_flips

# def minFlipsMonoIncr(s):
# 	ones = [0] * len(s)
# 	total_zero_count = 0
# 	min_flips = float('inf')
# 	for index, char in enumerate(s):
# 		if char == '0':
# 			ones[index] = ones[index - 1] if index != 0 else 0
# 			total_zero_count += 1
# 		else:
# 			ones[index] = (ones[index - 1] if index != 0 else 0) + 1
# 	cur_zero_count = 0
# 	print(ones)
# 	for index, char in enumerate(s):
# 		cur_flips = ones[index - 1] if index != 0 else 0
# 		if char == '0':
# 			cur_zero_count += 1
# 		cur_flips += (total_zero_count - cur_zero_count)
# 		min_flips = min(min_flips, cur_flips)
# 	return min_flips

# print('Output', minFlipsMonoIncr("00110"))
# print('Output', minFlipsMonoIncr("010110"))
# print('Output', minFlipsMonoIncr("00011000"))
print('Output', minFlipsMonoIncr("11011"))
# print('Output', minFlipsMonoIncr("100000001010000"))

"""
class Solution {
public:
    int minFlipsMonoIncr(string s) {
        int n = s.size();
        int one_counts = 0;
        vector<int> dp(n + 1);
        dp[0] = 0;
        
        for(int i = 1; i <= n; i++) {
            if(s[i - 1] == '1') {
                dp[i] = dp[i - 1];
                one_counts++;
            } else {
                dp[i] = min(dp[i - 1] + 1, one_counts);
            }
        }
        
        return dp[n];
    }
};
"""