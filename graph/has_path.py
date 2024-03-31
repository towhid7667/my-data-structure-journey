def has_path(graph, src, dst):
    if src == dst:
        return True
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst) is True:
            return True
    return False    

from collections import deque
def has_path_breadth(graph, src, dst):
    queue = deque([src])
    while queue:
        curr = queue.popleft()
        if curr == dst:
            return True
        for neighbor in graph[curr]:
            queue.append(neighbor)
    return False            