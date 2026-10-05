def eliminarUltimo(self):
    if self.tail:
        if self.tail==self.head:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
        self.size-=1
        