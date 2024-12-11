
class Stack:
    def __init__(self):
        self.stack = []
        self.reverse = ""
        
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()
        
    def reverse_sting(self):
        while len(self.stack) != 0:
            item = self.pop()
            self.reverse+= str(item)
            
    
    
s1 = Stack()

s1.push(10)
s1.push(20)
s1.push(30)
s1.reverse_sting()

# print(s1.stack)
print(s1.reverse)