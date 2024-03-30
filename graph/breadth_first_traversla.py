from collections import deque

def breadth_first_print(graph, start):
    queue = deque([start])
    while queue:
        curr = queue.popleft()
        print(curr)
        for neighbor in graph[curr]:
            queue.append(neighbor)


graph = {
    "a" : ["c" , "b"],
    "b" : ["d"],
    "c" : ["e"],
    "d" : ["f"],
    "e" : [],
    "f" : [],


}

breadth_first_print(graph, 'a')