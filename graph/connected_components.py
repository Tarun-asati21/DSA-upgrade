adj = {0: [1, 2], 1: [0, 2], 2: [1, 0]}

visited = [0]*len(adj)

def dfs(start):
    visited[start]=1
    for node in adj[start]:
        if visited[node] == 0 :
            dfs(node)

count=0
for i in range(len(adj)): # total nodes = len(adj)
    if visited[i] == 0 :
        dfs(i)
        count+=1
        
print(count)