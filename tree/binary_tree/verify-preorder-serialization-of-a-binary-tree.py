"""
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
"""

# OWN
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        need = 1
        preorder = preorder.split(',')
        for char in preorder:
            if need == 0:
                return False
            if char == '#':
                need -= 1
            else:
                need += 1
        return need == 0


public boolean isValidSerialization(String preorder) {
    String[] nodes = preorder.split(",");
    int diff = 1;
    for (String node: nodes) {
        if (--diff < 0) return false;
        if (!node.equals("#")) diff += 2;
    }
    return diff == 0;
}        


class Solution(object):
	def isValidSerialization(self, preorder):
	    """
	    :type preorder: str
	    :rtype: bool
	    """
	    stack = []
	    top = -1
	    preorder = preorder.split(',')
	    for s in preorder:
	        stack.append(s)
	        top += 1
	        while(self.endsWithTwoHashes(stack,top)):
	            h = stack.pop()
	            top -= 1
	            h = stack.pop()
	            top -= 1
	            if top < 0:
	                return False
	            h = stack.pop()
	            stack.append('#')
	        #print stack
	    if len(stack) == 1:
	        if stack[0] == '#':
	            return True
	    return False

	def endsWithTwoHashes(self,stack,top):
	    if top<1:
	        return False
	    if stack[top]=='#' and stack[top-1]=='#':
	        return True
	    return False