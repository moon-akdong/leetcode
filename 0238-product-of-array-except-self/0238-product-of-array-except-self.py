class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 좌우 곱셈 결과 
        def products(nums,sub=1):
            for num in nums:
                yield sub
                sub *= num
        result = [] 
        left = products(nums)
        right = list(products(nums[::-1]))[::-1]

        for ln, rn in zip(left,right):
            result.append(ln * rn)
        return result 



