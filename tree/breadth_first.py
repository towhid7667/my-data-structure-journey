from collections import deque

def breadth_first_search(root):
    if root is None:
        return []
    values = []
    queue = deque([root])

    while queue:
        curr = queue.popleft()
        values.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)  
    return values          