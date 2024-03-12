from collections import deque
def tree_includes(root, target):
    if root is None:
      return False
    queue = deque([root])
    while queue:
      curr = queue.popleft()
      if curr.val == target:
        return True
      if curr.left:
        queue.append(curr.left)
      if curr.right:
        queue.append(curr.right)
    return False

def tree_includes(root, target):
    if root is None:
      return False
    if root.val == target:
        return True
    return tree_includes(root.left, target) or tree_includes(root.right, target)