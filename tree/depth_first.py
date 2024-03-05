def dpth_first_values(root):
    if root is None : return [ ]
    values = []
    stack = [root]
    while stack:
        curr = stack.pop()
        values.append(curr.val)
        if curr.right is not None:
            stack.append(curr.left)
        if curr.left is not None:
            stack.append(curr.left)
    return values    



def dpth_first_values(root):
    if root is None : return [ ]
    left_value = dpth_first_values(root.left)
    right_value = dpth_first_values(root.right)
    return [root.val , *left_value , *right_value]



class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
  def getVal(self):
      return f'the value is {self.val}'
    
def depth_first_values(root):
  if root is None : return []
  left_value = depth_first_values(root.left)
  right_value = depth_first_values(root.right)
  
  return [root.val , *left_value , *right_value] 
    
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')        
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

depth_first_values(a)    