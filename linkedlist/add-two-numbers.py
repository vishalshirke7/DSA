"""
https://leetcode.com/problems/add-two-numbers/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number1, number2 = "", ""
        while l1:
            number1 = str(l1.val) + number1
            l1 = l1.next
        while l2:
            number2 = str(l2.val) + number2
            l2 = l2.next
        total = int(number1) + int(number2)
        new = ListNode(0)
        cur = new
        while total:
            rem = total % 10
            total //= 10
            node = ListNode(rem)
            cur.next = node
            cur = cur.next
        return new.next if new.next else new


"""
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode dummyHead = new ListNode(0);
    ListNode p = l1, q = l2, curr = dummyHead;
    int carry = 0;
    while (p != null || q != null) {
        int x = (p != null) ? p.val : 0;
        int y = (q != null) ? q.val : 0;
        int sum = carry + x + y;
        carry = sum / 10;
        curr.next = new ListNode(sum % 10);
        curr = curr.next;
        if (p != null) p = p.next;
        if (q != null) q = q.next;
    }
    if (carry > 0) {
        curr.next = new ListNode(carry);
    }
    return dummyHead.next;
}
"""        