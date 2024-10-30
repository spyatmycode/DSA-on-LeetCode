class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        for i in range(len(prices)):

            pointer = i + 1

            while pointer < len(prices):

                profit = max(profit, prices[pointer] - prices[i])

                pointer += 1
        

        return profit



           
                   
        
        return profit
        