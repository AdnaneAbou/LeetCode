class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"
        
    def is_empty(self):
        return len(self.stack) == 0   
    def size(self):
        return len(self.stack) 

stack = Stack()
stack.push(5)
stack.push(54)

print(stack.peek())
print(stack.pop())
print(stack.peek())