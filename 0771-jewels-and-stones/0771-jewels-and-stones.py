class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        table = collections.defaultdict(int) 
        count = 0 
        for char in stones:
            table[char] += 1

        for char in jewels:
            if char in table:
                count += table[char]
        
        return count 