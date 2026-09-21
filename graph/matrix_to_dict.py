import collections 

matrix = [[1,1,0],[0,0,1],[1,0,1]]

R,C = len(matrix), len(matrix[0])

adj = collections.defaultdict(list)
for i in range(R):
    for j in range(C):
        if matrix[i][j]==1 and i!=j :
            adj[i].append(j)
            adj[j].append(i)
        
print(adj)