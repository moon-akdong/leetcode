class Solution:
    def trap(self, height: List[int]) -> int:
        # left,right = 0, len(height)-1
        # left_max, right_max = height[left],height[right]
        # water = 0
        # while left < right:
        #     left_max, right_max = max(height[left],left_max), \
        #                             max(height[right],right_max)
        #     if left_max <= right_max:
        #         water += left_max - height[left]
        #         left +=1 
        #     elif left_max > right_max:
        #         water += right_max - height[right]
        #         right -=1 
        # return water
        
        # Stack 
        stack = [] 
        volume = 0 

        for i in range(len(height)):
            # 변곡점을 만나는 경우 
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not len(stack):
                    break 
                
                distance = i - stack[-1] -1
                waters = min(height[i], height[stack[-1]])-height[top]
                volume += distance * waters 
            stack.append(i)
        return volume
