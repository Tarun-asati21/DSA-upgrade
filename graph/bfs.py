from collections import deque
# deque data structure in python : either we append from right side or pop from left side - all happens in O(1)


# assuming 1 based graph : ie starting from index 1 
def bfs(n, adj, starting_node) :
    
    # in ans variable : I will store my answer
    ans = []
    # in visited I will mark the nodes, whom I visited
    visited = [0]*(n+1)
    
    queue = deque()
    queue.append(starting_node)
    visited[starting_node]=1    
    
    while len(queue)!=0 :
        e = queue.popleft()
        ans.append(e)
        for node in adj[e]:
            if visited[node] == 0 : # ie not visited
                queue.append(node)
                visited[node]=1
                
    return ans
    

n = 9  # no of nodes
adjacency_list = [
    [],
    [2,8],
    [1,3,4],
    [2],
    [2,5],
    [4,6],
    [5,7],
    [6,8],
    [1,7,9],
    [8]
]

print(bfs(9, adjacency_list, 1))
print(bfs(9, adjacency_list, 3))