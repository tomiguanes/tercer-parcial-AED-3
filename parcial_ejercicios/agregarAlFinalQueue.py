def queue (self, x):
    nuevo=Node(x)
    if self.head:
        self.tail.next=nuevo
        nuevo.prev=self.tail
        nuevo.next=self.head
        self.head.prev=nuevo
        self.tail=nuevo
    else:
        self.head=nuevo
        self.tail=nuevo
        nuevo.prev=nuevo
        nuevo.next=nuevo
 
    self.size+=1
        