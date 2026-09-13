
"""  
  Solve: 
  - first find tail from list
  - then update before tail node to none
  - tail connect to head and rest of the after head
  - but i see after implementation Time O(n x k) not accept in leetcode
  
  I see a pattern:
  - we can reduce k repetation by doing k % len(list),because len(list) = 5, k =7 then k = 2 thats more than enough to get solution

"""
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
    
    curr = dummy
    l = 0
    while curr.next:
        curr = curr.next
        l += 1 
    tail = curr 
    
    
    
        
            
    
   

values = [0,1,2]
li = makeList(values)
ro = rotate_list(li, 4)

curr = ro 

while curr:
    print (curr.val, end=(" "))
    curr = curr.next 
        
        