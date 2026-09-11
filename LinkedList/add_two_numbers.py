""" 
  - Add two numbers
  l1 = [2,4,3], l2 = [5,6,4]
  - We need digit1 , digit2, and carry if 6+4=10 add 0 carry 1
  - sum = digit1 +  digit2 + carry
  - if l1> l2 or l2> l1 and carry so add thats the loop condition
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

    

