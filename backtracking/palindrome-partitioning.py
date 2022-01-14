"""
https://leetcode.com/problems/palindrome-partitioning/
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def check_palindrome(st, en):
            while st < en:
                if s[st] != s[en]:
                    return False
                st += 1
                en -= 1
            return True
                
        def dfs(index, cur_path):
            if index >= len(s):
                result.append(cur_path)
                return
            for new_index in range(index, len(s)):
                if check_palindrome(index, new_index):
                    dfs(new_index + 1, cur_path + [s[index:new_index+1]])
        dfs(0, [])
                    
        return result