
class Node:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 


def makeList(values):
    node = [Node(val) for val in values]
    for i in range(len(values) - 1):
        node[i].next = node[i+1]
    return node[0]

def rotate_list(node, k):
    dummy = Node(0)
    dummy.next = node 
   
    if node is None or node.next is None or k == 0:
        return node 
    while k > 0:
        curr = dummy
        while curr.next:
            curr = curr.next
        tail = curr
        c = dummy
        while c.next.next:
            c = c.next
        c.next = None
        tail.next = dummy.next
        dummy.next = tail
        k -= 1
    return dummy.next
        
            
    
   

values = [0,1,2]
li = makeList(values)
ro = rotate_list(li, 4)

curr = ro 

while curr:
    print (curr.val, end=(" "))
    curr = curr.next 
        
        