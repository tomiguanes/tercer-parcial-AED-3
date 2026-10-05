 def eliminarUltimo(self):
        if self.head:
            if self.size==1:
                self.head=None
                self.tail=None
            else:
                self.tail=self.tail.prev
                self.tail.next=None
            self.size-=1