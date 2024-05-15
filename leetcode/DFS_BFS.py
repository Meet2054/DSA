
# WAP for DFS and BFS


# DFS
graph ={
        5: [3,7],
        3: [2,4],
        7: [8],
        4: [8],
        2: [],
        8: []
        }
visited=set()

def DFS(visited,graph,node):
    if(node not in visited):
        print(node)
        visited.add(node)
    for nighbour in graph[node]:
        DFS(visited,graph,nighbour)

DFS(visited,graph,5)


#BFS

graph = {
    5: [3, 7],
    3: [2, 4],
    7: [8],
    4: [8],
    2: [],
    8: []
}

visited = []
queue = []

def BFS(visited, graph, node, queue):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

BFS(visited, graph, 5, queue)


