"""
https://leetcode.com/problems/remove-duplicate-letters/

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

"""


def removeDuplicateLetters(s):
    last_occ = {c: i for i, c in enumerate(s)}
    stack = ["!"]
    Visited = set()
    
    for i, symbol in enumerate(s):
        if symbol in Visited: 
            continue
        
        while (symbol < stack[-1] and last_occ[stack[-1]] > i):
            Visited.remove(stack.pop())
       
        stack.append(symbol)
        Visited.add(symbol)        
    return "".join(stack)[1:]


"""
def removeDuplicateLetters(s):
    rindex = {c: i for i, c in enumerate(s)}
    result = ''
    for i, c in enumerate(s):
        if c not in result:
            while c < result[-1:] and i < rindex[result[-1]]: 
                result = result[:-1]
            result += c
    return result
"""    

print(removeDuplicateLetters('bcabc'))
print(removeDuplicateLetters('cbacdcbc'))