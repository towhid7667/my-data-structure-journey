

def tree_min_value(root):
    stack = [root]
    smallest = float("inf")
    while stack:
        curr = stack.pop()
        if curr.val < smallest:
            smallest = curr.val

        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)  
    return smallest 

def tree_min_value(root):
  if root is None:
    return float("inf")
  smallest_left = tree_min_value(root.left)
  smallest_right = tree_min_value(root.right)  
  
  return min(root.val, smallest_left, smallest_right)


from collections import deque
def tree_min_value(root):
    queue = deque([root])
    smallest = float("inf")
    while queue:
        curr = queue.popleft()
        if curr.val < smallest:
            smallest = curr.val

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)  
    return smallest 