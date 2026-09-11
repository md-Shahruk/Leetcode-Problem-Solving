class Node:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next


def makeList(values):
    node = [Node(val) for val in values]
    for i in range(len(values) - 1):
        node[i].next = node[i+1]
    return node[0] 


def odd_even_list(h):
    
    dummuy = Node(0)
    curr = dummuy
    
    odd = h 
    even = h.next
    
    while odd:
        curr.next = Node(odd.val)
        curr = curr.next 
        if odd.next:
            odd = odd.next.next
        else:
            break
    while even:
        curr.next = Node(even.val)
        curr = curr.next
        if even.next:
            even = even.next.next
        else:
            break
    return dummuy.next 
        

        
head = [2,1,3,5,6,4,7]
li = makeList(head)
odd_v = odd_even_list(li)

curr = odd_v 
while curr:
    print(curr.val, end=(" "))
    curr =curr.next 
