class Node:
    def __init__(self, val):
         self.val = val
         self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')

a.next = b
b.next = c
c.next = d
d.next = e

# A->b->c->d->E
# normal solution
def printList(head):
    current = head
    while current:
        print(current.val)
        current = current.next

# recursion solution
def printListRec(head):
    if head is None:
        return
    print(head.val)    
    printListRec(head.next)            

printListRec(a)