class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key=lambda x: (x.split(" ",1)[1:], x.split(" ",1)[0]))
        # split은 strip()을 해주고, 시작한다. 
        # split(" ",1) 공백을 한번만 split한다.
        
        return letters + digits