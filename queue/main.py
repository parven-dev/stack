
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        
    def enqueue(self, value):
        new_node = Node(value)
        
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        
    def dequeue(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.first = None
            self.last = None

        temp = self.first
        self.first = self.first.next
        temp.next  = None
        return temp.value      
             
            
            
        
    def display(self):
        temp = self.first
        while temp is not None:
            print(temp.value, end="->")
            temp = temp.next
        
            
    

q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.display()

print("after")

print(q1.dequeue())
