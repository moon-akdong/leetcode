class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ind_stack = [] 
        result = [0]*len(temperatures)

        for ind, val in enumerate(temperatures):
            
            while ind_stack and val > temperatures[ind_stack[-1]]:
                prev = ind_stack.pop()
                result[prev] = ind - prev 
            
            ind_stack.append(ind)
        return result 
