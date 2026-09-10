

class Node:
    def __init__(self, data=0, next=None):
        self.data = data 
        self.next = next


def makeList(values):
    node = [Node(val) for val in values]
    for i in range(len(values) - 1):
        node[i].next = node[i+1]
    return node[0]

def remove_duplicate(h):
    curr = h
    
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return h 

head = [1,1,2,3,3]

li = makeList(head)
dup = remove_duplicate(li)

cur = dup
while cur:
    print(cur.data, end=" ")
    cur = cur.next