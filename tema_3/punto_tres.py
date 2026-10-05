def insertarElemento(self, x, i):
    if 0<=i<=self.size:
        new=Node(x)
        if i==0:
            if self.head:
                new.next=self.head
                self.head.prev=new
            self.head=new
        else:
            curr=self.head
            for _ in range(i-1):
                curr=curr.next
            if curr.next:
                new.prev=curr
                new.next=curr.next
                curr.next.prev=new
                curr.next=new
            else:
                curr.next=new
                new.prev=curr
        self.size+=1