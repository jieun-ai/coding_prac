class LinkedList(object):
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value) # 새 노드를 추가
        if self.head == None: # head가 0이면 = 노드가 하나도 없다면
            self.head = new_node
            
        # 맨 뒤의 node가 new_node를 가리켜야 한다.
        else:
            current = self.head # head로부터 거처가야 함
            while (current.next):
                current = current.next
            current.next = new_node
            
li = LinkedList()
li.append(1)
li.append(2)
li.append(3)
li.append(4)