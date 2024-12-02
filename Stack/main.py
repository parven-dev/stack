class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top  =  new_node
        self.height  = 1
    
    def display(self):
        temp = self.top

        while temp is not None:
            print(temp.value)
            temp = temp.next
    
s1 = Stack(40)
print(s1.display())
    