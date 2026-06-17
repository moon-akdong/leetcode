class Solution:
    def trap(self, height: List[int]) -> int:
        # stack 
        stack = [] 
        volume = 0 
        for pos, hei in enumerate(height):
        # Inflection Point - 변곡점
            while stack and height[stack[-1]] < hei:
                # volume 을 구하는 공식 
                prev_pos = stack.pop() 

                if len(stack) == 0:
                    break 
                
                dist = (pos - stack[-1]) -1
                water_height = min(hei, height[stack[-1]]) - height[prev_pos]

                volume += dist * water_height

            # stack 쌓기
            stack.append(pos)
        return volume 

        