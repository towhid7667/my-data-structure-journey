# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def sum_list(head):
    if head is None:
      return 0
    return head.val + sum_list(head.next)



def sum_list(head):
    sum = 0
    curr = head
    while curr:
      sum += curr.val
      curr = curr.next
    return sum    