def largest_component(graph):
  largest = 0
  visited = set()
  for node in graph:
    size = explore(graph, node, visited)
    if size > largest:
      largest = size
  return largest
def explore(graph, current, visited):
  if current in visited:
    return 0
  visited.add(current)
  size = 1
  for neighbor in graph[current]:
    size += explore(graph, neighbor, visited)
  return size    