graph = {
    "a" : ["c" , "b"],
    "b" : ["d"],
    "c" : ["e"],
    "d" : ["f"],
    "e" : [],
    "f" : [],


}

def depth_first_traversal(graph, start):
    stack = [start]
    while stack:
        curr = stack.pop()
        print(curr)
        for neighbor in graph[curr]:
            stack.append(neighbor)    
def depth_first_traversal_recursive(graph, curr):
    print(curr)
    for neighbor in graph[curr]:
        depth_first_traversal_recursive(graph, neighbor)
    



depth_first_traversal(graph, "a")
depth_first_traversal_recursive(graph, "a")            
