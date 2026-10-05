#eliminar el nodo i-ésimo
def eliminar(self):
    if 0<=i<self.size:
        if i==0:
            self.head=self.head.next
        else:
            aux=self.head
            for _ in range(i-1):
                aux=aux.next
            aux.next=aux.next.next
        self.size-=1