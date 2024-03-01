# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def zipper_lists(head_1, head_2):
  tail = head_1
  curr_1 = head_1.next
  curr_2 = head_2
  count = 0
  while curr_1 and curr_2:
    if count % 2 == 0:
      tail.next = curr_2
      curr_2 = curr_2.next
    else:
      tail.next = curr_1
      curr_1 = curr_1.next
    tail = tail.next
    count += 1
  if curr_1 : tail.next = curr_1
  if curr_2 : tail.next = curr_2
  return head_1



def zipper_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None
  if head_1 is None:
    return head_2
  if head_2 is None:
    return head_1
  
  next1 = head_1.next
  next2 = head_2.next
  
  head_1.next = head_2
  head_2.next = zipper_lists(next1, next2)
  return head_1  