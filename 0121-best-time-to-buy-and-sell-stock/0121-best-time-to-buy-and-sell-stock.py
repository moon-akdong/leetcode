class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num = sys.maxsize
        profit = -sys.maxsize
        if not prices:
            return 0 
            
        for p in prices:
            min_num = min(p,min_num)
            profit = max(profit, p - min_num)

        return profit 
            