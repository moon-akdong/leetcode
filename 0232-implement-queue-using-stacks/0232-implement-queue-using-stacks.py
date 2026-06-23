class MyQueue:

    def __init__(self):
        self.stack = [] 
        self.sub = [] 

    def push(self, x: int) -> None:
        # 여기서 뒤집으면 순서가 꼬임 
        self.stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.sub.pop()

    def peek(self) -> int:
        # return self.stack[0] 이렇게 하면 안됨 stack[-1]로 조회 햇을때 
        if not self.sub:
            for _ in range(len(self.stack)):
                self.sub.append(self.stack.pop())
        
        return self.sub[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.sub) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()