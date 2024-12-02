class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.top  =  None
        self.height  = 1
    
    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
            
    def display(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
s1 = Stack()
s1.push(50)
s1.push(60)
s1.push(60)
print(s1.display())
    