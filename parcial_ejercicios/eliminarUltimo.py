class Node:
    def __init__(self, x):
        self.data=x
        self.next=none
        #self.prev=none
        
        
class sll:
    def __init__(self):
        self.head=none
        self.tail=none
        self.size=0
        
    def eliminarUltimo(self):
        if self.head:
            if self.size==1:
                self.head=none
                self.tail=none
            else:
                prev=self.head #Probar otras opciones en la asignación principal
                curr=self.head
                while curr.next:
                    prev=curr
                    curr=curr.next
                prev.next=None
                self.tail=prev
            self.size-=1
            
    


def __repr__(self):
    c=self.head
    ret=[]
    while (c):
        ret.append(c.data)
        c=c.next
        return str(ret)
    
print(L)
print(eliminarUltimo(L))
        
        