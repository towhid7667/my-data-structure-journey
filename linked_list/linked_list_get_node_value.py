# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def get_node_value(head, index):
  count = 0
  curr = head
  while curr:
    if count == index:
      return curr.val
    count += 1
    curr = curr.next

def get_node_value(head, index):
  if head is None:
    return None
  if index == 0:
    return head.val
  return get_node_value(head.next, index - 1)    