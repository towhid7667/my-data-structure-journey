# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None


# recursion
def linked_list_values(head):
  k = []
  def kreturn(head, k):
      if head is not None:
         k.append(head.val)
         kreturn(head.next, k) 
  kreturn(head, k)        
  return k

# normal way
def linked_list_values(head):
  k = []
  curr = head
  while curr:
    k.append(curr.val)
    curr = curr.next
  return k
