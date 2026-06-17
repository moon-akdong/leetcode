class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 종료 조건
        result = [] 
        if len(nums) == 3:
            if sum(nums) == 0:
                result.append(nums)
            return result 

        # two pointer
        nums.sort()
        for ind,num in enumerate(nums):
            # 중복 제거 
            if ind != 0 and num == nums[ind-1]:
                continue 

            remain = nums[ind+1:]
            left, right = 0, len(remain) -1 

            while left < right:
                if (s:=num + remain[left] + remain[right]) > 0 :
                    right -= 1
                elif s < 0:
                    left +=1 
                else:
                    result.append([num,remain[left],remain[right]])
                    # 중복 제거
                    while left < right and remain[left] == remain[left+1]:
                        left +=1 
                    while left < right and remain[right] == remain[right-1]:
                        right -=1
                    left +=1 
                    right -=1 
        return result




