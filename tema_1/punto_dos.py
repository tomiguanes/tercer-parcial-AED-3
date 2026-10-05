def eliminarPrimero(self):
    if self.head:
        self.head=self.head.next
        self.size-=1