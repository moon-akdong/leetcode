class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = [] 
        letter = []
        for log in logs:
            ident, lg = log.split(' ',1)
            if lg.split()[0].isdigit():
                digit.append(log)
            else:
                letter.append(log)
        letter.sort(key = lambda x: (x.split(' ',1)[1], x.split(' ',1)[0]))
        result = letter + digit
        return result 