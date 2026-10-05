class Stack:
    def __init__(self):
        self.top=None
        self.size=0
        
    def push(self,value):
        n=Node(value)
        n.next=self.top
        self.top=n
        self.size+=1
        
    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.data
    
    def push2(self, value):
        if value!=self.peek():
            self.push(value)
            
    #sin peek
        if self.top.data!=value
        self.push(value)
        
    #doblemente enlazada
    def push(self,value):
        n=Node(value)
        n.next=self.top
        self.top.prev=n
        self.top=n
        self.size+=1
        