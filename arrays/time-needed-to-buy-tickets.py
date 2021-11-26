"""
https://leetcode.com/problems/time-needed-to-buy-tickets/
"""


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = tickets[k]
        for index in range(0, k):
            total += min(tickets[index], tickets[k])
        for index in range(k + 1, len(tickets)):
            total += min(tickets[index], tickets[k] - 1)
        return total


"""
class Solution {
public:
    int timeRequiredToBuy(vector<int>& A, int k) {
        int ans = 0;
        for (int i = 0; i < A.size(); ++i) {
            ans += min(A[k] - (i > k), A[i]);
        }
        return ans;
    }
};        
"""