class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None
    
    def trampa(self):
    
            

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
        
    def queue(self, data):
        new=Node(data)
        if self.head is None:
            self.head=new
            self.tail=new
        else:
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
        self.size+=1
    
    def dequeue(self):
        if self.head:
            data=self.head.data
            if self.head==self.tail
                self.head=None
                self.tail=None
            else:
                self.head=self.head.next
                self.head.prev=None
            return data
        else:
            return "Lista vacia"