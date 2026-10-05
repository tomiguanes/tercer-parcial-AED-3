class Nodo:
    def __init__(self, data):
        self.data=data
        self.next=None
        
class Stack:
    def push(self,x):
        new=Nodo(x)
        new.next=self.head
        self.head=new
    
    def pop(self):
        if self.head:
            data=self.head.data
            self.head=self.head.next
            return data
    
    def push2(self, x):
        if self.head is None or self.head.data!=x:
            self.push(x)
                
                
            
                
        