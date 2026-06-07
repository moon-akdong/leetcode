class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def element_product(nums,sub=1):
            for e in nums:
                yield sub
                sub = sub * e
                
        it = element_product(nums)
        it2 = element_product(nums[::-1])
        ls = list(it)
        ls2 = list(it2)[::-1]
        result = [] 
        for i in range(len(ls)):
            result.append(ls[i] * ls2[i])
        return result