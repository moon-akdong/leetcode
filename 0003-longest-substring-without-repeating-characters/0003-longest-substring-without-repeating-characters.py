class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1 :
            return 1
        elif len(s) == 0:
            return 0 

        start, end = 0,0
        length = 0 
        used = collections.defaultdict(int)

        for ind,char in enumerate(s):
            print(ind,start, char)
            if char in used and start <= used[char]:
                start = used[char] + 1 

            else:
                length = max(length, ind - start + 1)
            used[char] = ind
            print(length)
        return length


        # while end < len(s):
        #     char = s[end]
        #     print(end,char)
        #     if char in used:
        #         start=used[char] + 1
            
        #     else:
        #         length = max(length, end - start + 1)
        #         used[char] = end
        #     end +=1 
        #     print(length)
        # return length 

