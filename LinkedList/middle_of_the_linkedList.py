
'''
  - first we make list size half 
  - then run a loop 0 to len(list)
  - and where loop end print this val
  - Time: O(n)

'''


class Node:
    def __init__(self, data=0, next=None):
        self.data = data 
        self.next = next

def makeNodeList(values):
    node = [Node(val) for val in values]
    for i in range(len(values) - 1):
        node[i].next = node[i+1]
    return node[0]

def middleofList(head):
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

head = [1,2,3,5,4,5]
li = makeNodeList(head)
mid = middleofList(li)

print(mid)

