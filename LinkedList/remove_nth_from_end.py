

""" 
   Solve:
   - this is singly linkedlist, so it's tough to travarse end to first
   - but using two pointer approach it is possible to travarse
   - take f and s and f start n step ahead
   - while there is no f.next then the point s.next is the one step ahead what we want to delete just shift next value
   - Time: O(n) and Space: O(1)
   
   - also brute force can solve this just handle extra variable for calculate len

"""

class Node:
    def __init__(self,data=0, next=None):
        self.data =data 
        self.next = next 


class LinkedList:
    def __init__(self):
        self.dummy_node = Node(0)
        self.size = 0
        
    def addlast(self, val):
        new_node = Node(val)
        curr = self.dummy_node
        for _ in range(self.size):
            curr = curr.next
        curr.next = new_node
        self.size += 1
        
    # def deleteNthEnd(self, n):
    #     f = self.dummy_node
    #     s = self.dummy_node
        
    #     for _ in range(n):
    #         f = f.next
        
    #     while f.next:
    #         s = s.next
    #         f = f.next
    #     s.next = s.next.next 
    
    def deleteNthEnd(self, n):
        
        curr = self.dummy_node
        l = 0
        
        while curr.next:
            l += 1
            curr = curr.next
        
        p = l - n + 1
        
        curr = self.dummy_node
        for _ in range(p-1):
            curr = curr.next
        curr.next = curr.next.next
            
        
    def printList(self):
        curr = self.dummy_node.next
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
            
    
li = LinkedList()
li.addlast(1)
li.addlast(2)
li.addlast(3)
li.addlast(4)
li.addlast(5)
li.addlast(6)
li.addlast(7)
li.addlast(8)



li.printList()
print("\n")
li.deleteNthEnd(8)
li.printList()