def eliminar(self, i):
    if 0<=i<self.size:
        if i==0:
            self.head=self.head.next        
        else:
            curr=self.head
            for _ in range (i-1):
                curr=curr.next 
            curr.next=curr.next.next     
        self.size-=1   
        
            