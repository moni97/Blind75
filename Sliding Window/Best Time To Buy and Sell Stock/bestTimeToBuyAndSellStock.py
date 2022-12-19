def maxProfit(self, prices: List[int]) -> int:
       buy = prices[0]
       profit = 0
       for i in range(1, len(prices)):
           if (prices[i] - buy > 0):
               profit = max(profit, prices[i] - buy)
           else:
                buy = prices[i]
       return profit
