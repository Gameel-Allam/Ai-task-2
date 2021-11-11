adj_list = {'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['B', 'F'],
            'D': [],
            'E': ['F'],
            'F': [], }
color = {}
parent = {}
traversal_time = {}
dfs_out = []
for node in adj_list:
    color[node] = 'W'
    parent[node] = None
    traversal_time[node] = [-1, -1]
time = 0


def dfs(u):
    global time
    color[u] = 'G'
    traversal_time[u][0] = time
    dfs_out.append(u)
    for v in adj_list[u]:
        if color[v] == 'W':
            parent[v] = u
            dfs(v)
    color[u] = 'B'
    traversal_time[u][1] = time
    time += 1


dfs('A')
print(color)
print(parent)
print(traversal_time)
print(dfs_out)
print()
for node in adj_list.keys():
    print()
    print(node, "==>", traversal_time[node])
