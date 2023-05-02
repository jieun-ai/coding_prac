# Linked list 중간에 노드를 추가한다.

class LinkedList(object):
    def __init__(self):
        self.head = None
    def append(self, value):
        pass
    def insert(self, idx, value):
        new_node = Node(value)
        current = self.head
        for _ in idx-1:
            current = current.next
            new_node.next = current.next
        current.next = new_node
    
li = LinkedList()
li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.insert(idx = 2, value = 9)

## 실제 정답
def insert(self, idx, value):
    new_node = Node(value)

    if idx == 0:
        new_node.next = self.head # self.head가 원래 기존의 첫번째 박스를 가리켰는데
        self.head = new_node # 새로 들어온 new_node로 head를 변경함

    else:
        current = self.head

        for _ in range(idx-1):
            current = current.next
        new_node.next = current.next
        current.next = new_node     
