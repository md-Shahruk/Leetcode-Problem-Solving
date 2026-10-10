class Node:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 


def make_node(values):
    nodes = [Node(val) for val in values]
    for i in range(len(values) - 1):
        nodes[i].next = nodes[i+1]
    return nodes[0]

def make_intersection(nodeA, nodeB, intersect, skipA, skipB): 
    curA = nodeA
    curB = nodeB
    
    for _ in range(skipA - 1):
        curA = curA.next
    for _ in range(skipB - 1):
        curB = curB.next 
        
    cur_1 = nodeA
    cur_2 = nodeB
    if curA.next.val == intersect and curB.next.val == intersect:
        curA.next = curB.next
     
    return curA
    


values1 = [4,1,8,4,5]
values2 = [5,6,1,8,4,5]

nodeA =  make_node(values1)
nodeB = make_node(values2)


li = make_intersection(nodeA, nodeB,8, 2, 3)
curr = li 
while curr:
    print(curr.val, end=(" "))
    curr = curr.next 
