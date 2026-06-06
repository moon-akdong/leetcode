class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned ]
        
        words_count = collections.Counter(words)
        print(words_count)
        return max(words_count, key=words_count.get)