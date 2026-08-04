
'''
Target:
   - Add first and last
   - Print list
   - Add position based
   - Search value
   - Delete first and last
   - Delete position based
'''

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def addFirst(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1
        
    
    def addLast(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def deleteFirst(self):
        self.head = self.head.next
        self.size -= 1
        if self.head is None:
            self.tail = None
         
    
    def deleteLast(self):
        cur = self.head
        while cur.next.next is not None:
            cur = cur.next
        
        cur.next = None
        self.tail = cur 
        self.size -= 1
    
    def add_positonBased(self, data, position):
        if position < 0 or position > self.size:
            return 
        if position == 0:
            self.addFirst(data)
            return
        if position >= self.size:
            self.addLast(data)
            return
        new_data = Node(data)
        cur = self.head
        for i in range(position - 1):
            cur = cur.next
        new_data.next = cur.next
        cur.next = new_data
        self.size += 1
        
    
    def printList(self):
        current = self.head
        while current is not None:
            print(current.data, end=("-"))
            current = current.next
        print("None")

l = LinkedList()
l.addFirst(10)
l.addFirst(5)
l.addFirst(1)

l.addLast(20)
l.printList()
l.deleteFirst()
l.printList()
l.deleteLast()
l.printList()
l.add_positonBased(7,1)
l.printList()

        
