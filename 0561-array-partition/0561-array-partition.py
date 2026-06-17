class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        s = 0 
        pair = [] 
        nums.sort()
        
        for n in nums:
            pair.append(n)
        
            if len(pair) == 2:
                s += min(pair)
                pair = [] 
        return s 