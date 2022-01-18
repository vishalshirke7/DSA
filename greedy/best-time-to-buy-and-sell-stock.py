"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/851941/Python-O(n)-dynamic-programming-solution-explained
"""
"Kadane's Algorithm"

public class Solution {
    public int maxProfit(int prices[]) {
        int minprice = Integer.MAX_VALUE;
        int maxprofit = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minprice)
                minprice = prices[i];
            else if (prices[i] - minprice > maxprofit)
                maxprofit = prices[i] - minprice;
        }
        return maxprofit;
    }
}

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right_max = [0] * len(prices)
        right_max[len(prices) - 1] = prices[len(prices) - 1]
        for index in range(len(prices) - 2, -1, -1):
            right_max[index] = max(prices[index], right_max[index + 1])
        # print(right_max)
        max_p = 0
        for index in range(len(prices)):
            max_p = max(max_p,  right_max[index] - prices[index])
        return max_p
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:            
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit        