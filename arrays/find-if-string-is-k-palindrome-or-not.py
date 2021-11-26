"""
https://www.geeksforgeeks.org/find-if-string-is-k-palindrome-or-not/
"""

def is_valid(ip_st, start, end, k, dp):
	key = "{}".format(start) + "{}".format(end)
	if key in dp:
		return dp[key]
	while start < end:
		if ip_st[start] != ip_st[end]:
			if k == 0:
				dp[key] = 0
			else:
				dp[key] = is_valid(ip_st, start + 1, end, k - 1, dp)
				if not dp[key]:
					dp[key] = is_valid(ip_st, start, end - 1, k - 1, dp)
		start += 1
		end -= 1
	if key in dp:
		return dp[key]		
	return 1

def kPalindrome(str, n, k):
	return is_valid(str, 0, n- 1, k, {})


# print('Output', kPalindrome("abcdecba", 8, 1))
# print('Output', kPalindrome("abcdefcba", 9, 1))	
print('Output', kPalindrome("qwewretytuiop", 13, 7))