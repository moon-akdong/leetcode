class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        chars = [char for char in re.sub('[^\w]',' ',paragraph).lower().split() if char not in banned]
        counts = collections.Counter(chars)

        return counts.most_common(1)[0][0] # Counter.most_common 