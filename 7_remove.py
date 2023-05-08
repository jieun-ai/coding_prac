def remove(self, idx):
    if idx == 0:
        self.head = self.head.next # garbage collector가 알아서 처리해준다.
    else:
        current = self.head
        for _ in range(idx-1): 
            current = current.next
        current.next = current.next.next 