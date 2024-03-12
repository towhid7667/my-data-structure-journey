from collections import deque
def tree_sum(root):
    if root is None:
        return 0
    queue = deque([root])
    total_sum = 0
    while queue:
        curr = queue.popleft()
        total_sum += curr.val
        if curr.left:
            queue.append(curr.left) 
        if curr.right:
            queue.append(curr.right)      
    return total_sum

def tree_sum(root):
  if root is None:
    return 0
  stack = [root]
  sum = 0
  while stack:
    curr = stack.pop()
    sum += curr.val
    if curr.right:
      stack.append(curr.right)
    if curr.left:
      stack.append(curr.left)  
  return sum 

def tree_sum(root):
  if root is None:
    return 0
  return root.val +  tree_sum(root.left) +  tree_sum(root.right) 