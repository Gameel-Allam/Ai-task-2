from queue import Queue
adj_list = {'A': ['B', 'D'],
            'B': ['A', 'C'],
            'C': ['D'],
            'D': ['A', 'E', 'F'],
            'E': ['D', 'F', 'G'],
            'F': ['D', 'E', 'H'],
            'G': ['E', 'H'],
            'H': ['F', 'G'], }
visited = {}
level = {}
parent = {}
bfs_out = []
queue = Queue()
for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

print(visited)
print(level)
print(parent)

u = 'A'
visited[u] = True
level[u] = 0
queue.put(u)

while not queue.empty():
    u = queue.get()
    bfs_out.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u]+1
            queue.put(v)
v = 'G'
path = []
while v is not None:
    path.append(v)
    v = parent[v]
path.reverse()

print(bfs_out)
print(level)
print(path)
