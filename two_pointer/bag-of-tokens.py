"""
https://leetcode.com/problems/bag-of-tokens/
"""



def bagOfTokensScore(tokens, power):
	tokens.sort()
	start, end, max_score, cur_score = 0, len(tokens) - 1, 0, 0
	while start <= end:
		if tokens[start] <= power:
			power -= tokens[start]
			cur_score += 1
			max_score = max(max_score, cur_score)
			start += 1
		elif max_score >= 1:
			power += tokens[end]
			cur_score -= 1
			max_score = max(max_score, cur_score)
			end -= 1
		else:
			break
	return max_score



print('Output', bagOfTokensScore([100], 50))
print('Output', bagOfTokensScore([100, 200], 150))
print('Output', bagOfTokensScore([100,200,300,400], 200))
