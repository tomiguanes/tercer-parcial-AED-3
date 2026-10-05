def insertarElemento(self, x, i):
    if 0<=i<=self.size:
        nuevo=Node(x)
        if i==0: ## agrego al principio
            if self.head: ## la lista no está vacía
                nuevo.next=self.head
                self.head.prev=nuevo
            self.head=nuevo 
        else:
            curr=self.head
            
            for _ in range (i-1):
                curr=curr.next
            
            nuevo.next=curr.next
            nuevo.prev=curr
            
            if curr.next:
                curr.next.prev=nuevo
            
            curr.next=nuevo
        self.size+=1
    
    else:
        raise ValueError("k debe pertenecer al rango de la lista")
        
    
        
        
        
        