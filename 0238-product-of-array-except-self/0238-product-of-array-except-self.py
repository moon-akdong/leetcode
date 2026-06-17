class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [] 
        p = 1 
        for i in range(0,len(nums)):
            out.append(p)
            p = p*nums[i]
        p = 1
        for i in range(len(nums)-1,0-1,-1):
            out[i] = out[i] * p
            p = p* nums[i]
        return out
        # def element_product(nums,sub=1):
        #     for e in nums:
        #         yield sub
        #         sub = sub * e
                
        # it = element_product(nums)
        # it2= element_product(nums[::-1])
       
        # ls = list(it)
        # ls2 = list(it2)[::-1]
        # result = [] 
        # for i in range(len(ls)):
        #     result.append(ls[i] * ls2[i])
        # return result