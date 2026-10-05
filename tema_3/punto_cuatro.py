class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None
    
    def validar (self, f):
        if not f(self.data):
            if self.prev:
                self.prev.next=self.next
            if self.next:
                self.next.prev=self.prev
            self.prev=None
            self.next=None
                

class Stack:
    def __init__(self):
        self.head=None
        self.size=0
    
    def push(self, x):
        new=Node(x)
        if self.head:
            new.next=self.head
            self.head.prev=new
        self.head=new
        self.size+=1
        
    def pop(self):
        if self.head:
            data=self.head.data
            self.head=self.head.next
            if self.head:
                self.head.prev=None
            self.size-=1
            return data
        