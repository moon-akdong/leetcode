class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer 
        volume = 0 
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            # 현재 높이와 이전 제일 높은 높이 비교 
            left_max, right_max = max(left_max, height[left]), max(right_max,height[right])
            
            if left_max < right_max:
                volume += left_max - height[left]
                left +=1 
            
            elif left_max >= right_max:
                volume += right_max - height[right]
                right -=1 

        return volume 


