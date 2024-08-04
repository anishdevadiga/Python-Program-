from collections import defaultdict, deque
#begin
def countGoodEdge(n, a, p):
    tree = defaultdict(list)
    for i in range(n):
        if i != p[i]:  
            tree[i].append(p[i])
            tree[p[i]].append(i)
    
    #begin
    def bfs(start, removedEdge):
        queue = deque([start])
        visited = set([start])
        values = set([a[start]])
        while queue:
            node = queue.popleft()
            for neighbor in tree[node]:
    
                if (node, neighbor) == removedEdge or (neighbor, node) == removedEdge:
                    continue
                if neighbor not in visited:
                    if a[neighbor] in values:
                        return False
                    visited.add(neighbor)
                    values.add(a[neighbor])
                    queue.append(neighbor)
        return True
    #end 
    countEdges = 0
    for i in range(n):
        if i == p[i]:  
            continue
    
        if bfs(i, (i, p[i])) and bfs(p[i], (i, p[i])):
            countEdges += 1
    
    return countEdges

#end
N = 2
A = [1, 1]
P = [0, 1]
result = countGoodEdge(N, A, P)
print(result)  
print(2**(3**2))
