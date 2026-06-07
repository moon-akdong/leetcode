class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        if not height:
            return volume 
        
        left,right = 0, len(height)-1 
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max,height[right])
        
            if left_max < right_max: 
                volume += left_max - height[left]
                left +=1 
            elif left_max >= right_max:
                volume += right_max - height[right]
                right-=1 
        return volume

        

