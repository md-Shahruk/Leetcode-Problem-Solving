

""" 
   Solve:
   - list  1 2 3
   - first think we set none after 1 : 1 - none
   - then take 2 and set before 1: 2 - 1 - none ..rest of the whole list
   - so we can track next value using n = curr.next 
   - and first time prve = none and after every time we can update prev every front node
"""

class Node:
    def __init__(self, data=0, next=None):
        self.data = data 
        self.next = next 


def makeList(values):
    node = [Node(val) for val in values]
    for i in range(len(values) - 1):
        node[i].next = node[i+1]
    return node[0]

def reverseList(node):
    p = None 
    curr = node 
    while curr:
        n = curr.next
        curr.next = p 
        p = curr
        curr = n 
    return p
        

values = [1,2,3,4,5]
li = makeList(values)
rev = reverseList(li)

curr = rev 
while curr:
    print(curr.data, end=(" "))
    curr = curr.next