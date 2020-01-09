class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(1,len(prices)):
            if (prices[i]>prices[i-1]):
                profit+=prices[i]-prices[i-1]
        return profit
#greedy means that we will only consider the best choice under current situation. and it wiil lead us to the global optimization.
#the local optimization is that we will buy the stock if today's price is lower that tomorrow's price
 