"""
https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
"""

def minInsertions(s):
	open_b, ans, index = 0, 0, 0
	while index < len(s) - 1:
		if s[index] == '(':
			open_b += 1
			index += 1
		elif s[index] == ')' and s[index + 1] == ')':
			if open_b:
				open_b -= 1
			else:
				ans += 1
			index += 2
		elif s[index] == ')' and s[index + 1] != ')':
			if open_b:
				open_b -= 1
				ans += 1
			else:
				ans += 2
			index += 1
	if index == len(s) - 1:
		if s[index] == '(':
			open_b += 1
		else:
			if open_b:
				open_b -= 1
				ans += 1
			else:
				ans += 2
	return ans + (open_b * 2)



print('Output', minInsertions("(()))"))

"""
    def minInsertions(self, s):
        res = right = 0
        for c in s:
            if c == '(':
                if right % 2:
                    right -= 1
                    res += 1
                right += 2
            if c == ')':
                right -= 1
                if right < 0:
                    right += 2
                    res += 1
        return right + res
"""