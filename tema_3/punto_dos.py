def eliminarUltimo(self):
    ##lista vacía
    if not self.head:
        return
    if self.head:
        if self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            curr=self.head
            while curr.next is not self.tail:
                curr=curr.next
            curr.next=None
            self.tail=curr
        self.size-=1
   
        