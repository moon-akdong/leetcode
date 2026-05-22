class Solution:
    # 투포인터가 슬라이딩 원도우 처럼 움직임
    def longestPalindrome(self, s: str) -> str:
        # 조기 종료 조건 
        def expand(left:int,right:int):
            while left >= 0 and right<len(s) and s[left] == s[right]:
                # s[left] == s[right-1] : 홀수에서 중앙점 
                # 짝수에서 같은지
                left -=1 
                right +=1 
            return s[left+1:right] # 이전 while 문을 통과할때 값
        
        if len(s) < 2 or s == s[::-1]:
            return s 
        result = ''
        for i in range(len(s)-1):
            print(i)
            print("first:",expand(i,i+1),"second",expand(i,i+2))
            result = max(result,
                            expand(i,i+1),
                            expand(i,i+2),
                            key=len)
        return result
    
        