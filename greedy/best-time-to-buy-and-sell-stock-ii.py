"""
https://www.geeksforgeeks.org/stock-buy-sell/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
https://interviewbit.com/old/problems/best-time-to-buy-and-sell-stocks-ii/
"""
def maxProfit(prices):
    left_small, cur_profit, max_profit = 10 ** 4, 0, 0
    for index in range(len(prices)):
        if prices[index] < left_small and cur_profit == 0:
            left_small = prices[index]
        elif prices[index] - left_small > cur_profit:
            cur_profit = prices[index] - left_small
        else:
            left_small = prices[index]
            max_profit += cur_profit
            cur_profit = 0
    max_profit += cur_profit
    return max_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2,3,4,5]))
print(maxProfit([7,6,4,3,1]))   
print(maxProfit([2,1,2,0,1]))   

"""
class Solution {
    public int maxProfit(int[] prices) {
        int maxprofit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1])
                maxprofit += prices[i] - prices[i - 1];
        }
        return maxprofit;
    }
}
"""