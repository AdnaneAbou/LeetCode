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


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    dictionary = {
        '(':')',
        '[':']',
        '{':'}',
    }
    stack = Stack()
    stack.push(s[0])
    for i in range(len(s)-1):
        if(stack.is_empty()):
            stack.push(s[i+1])
            print("s[i+1] : ",s[i+1])
        elif  stack.peek() in dictionary and dictionary[stack.peek()] == s[i+1] :
            stack.pop()
        else :
            stack.push(s[i+1])

        
    print("sfdvs",stack.peek())

    if stack.is_empty():
        return True
    else :
        return False
    

s="({}}{"

print(isValid(s))
