class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0

# Test
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    print(f"Stack: {stack.items}")
    print(f"Peek: {stack.peek()}")
    print(f"Pop: {stack.pop()}")
    print(f"Final: {stack.items}")