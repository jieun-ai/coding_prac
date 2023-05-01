# idx 번째에 있는 값을 뽑는다

class LinkedList(object):
    def __init__(self):
        self.head = None
    def append(self, value):
        pass
    def get(self, idx):
        current = self.head
        for _ in idx:
            current = current.next
        return current.value
    
li = LinkedList()
li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.get(0)
li.get(1)
li.get(3)
