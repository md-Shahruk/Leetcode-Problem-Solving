
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = None 

def makeList(values, pos):
    node = [Node(val) for val in values]
    for i in range(len(values) - 1):
        node[i].next = node[i+1]
    if pos > -1 and pos < len(values):
        node[-1].next = node[pos]
    return node[0]


def list_Cycle(head):
    
    s= f = head
    while f and f.next:
        s = s.next
        f = f.next.next
        if s == f:
            return True
    else:
        return False

values = [1,2,3,4]
pos = -1

li = makeList(values, pos)
print(list_Cycle(li))

        
    