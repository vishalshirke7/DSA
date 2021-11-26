"""
https://leetcode.com/problems/palindrome-linked-list/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def getVal(self, start):
        if start.next:
            nextVal = self.getVal(start.next)
            if nextVal is None:
                return start.val
            return nextVal
        else:
            val = start.val
            start.val = None
            return val
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        while cur and cur.next:
            last_val = self.getVal(cur.next)
            if last_val is None:
                return True
            if last_val == cur.val:
                cur = cur.next
            else:
                return False
        return True


def isPalindrome(self, head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev


class Solution {
public:
    ListNode* temp;
    bool isPalindrome(ListNode* head) {
        temp = head;
        return check(head);
    }
    
    bool check(ListNode* p) {
        if (NULL == p) return true;
        bool isPal = check(p->next) & (temp->val == p->val);
        temp = temp->next;
        return isPal;
    }
};    

def isPalindrome(self, head):
    fast = slow = head
    # find the mid node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse the second half
    node = None
    while slow:
        nxt = slow.next
        slow.next = node
        node = slow
        slow = nxt
    # compare the first and second half nodes
    while node: # while node and head:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True