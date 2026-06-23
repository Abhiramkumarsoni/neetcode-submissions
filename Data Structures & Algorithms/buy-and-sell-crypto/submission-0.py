class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=[0]
        for i in range(len(prices)-1):
            for j in range(i + 1,len(prices)):
                p=prices[j]-prices[i]
                profit.append(p)
        return max(profit)
