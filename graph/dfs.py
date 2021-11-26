"""https://www.hackerearth.com/practice/notes/karthic-hackintosh/simple-explanation-of-implementation-of-dfs-in-python/"""

# 1. Disconnected Graph

def dfs(G,node,traversed):
    traversed[node]=True #mark the traversed node 
    dfs.append(node.data)
    for neighbour_nodes in G[node]: #take a neighbouring node 
        if neighbour_nodes not in traversed: #condition to check whether the neighbour node is already visited
            dfs(G,neighbour_nodes,traversed) #recursively traverse the neighbouring node

def start_traversal(G):
    traversed = {} #dictionary to mark the traversed nodes 
    for node in G.keys(): #G.keys() returns a node from the graph in its iteration
        if node not in traversed: #you start traversing from the root node only if its not visited 
            dfs(G,node,traversed); #for a connected graph this is called only once

start_traversal(G)


# 2. O(V + E)
class Solution:
    
    def dfs_traverse(self, vertex, visited, adj, dfs):
        visited.add(vertex)
        dfs.append(vertex)
        for adj_vertex in adj[vertex]:
            if adj_vertex not in visited:
                self.dfs_traverse(adj_vertex, visited, adj, dfs)
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited = set()
        dfs = list()
        self.dfs_traverse(0, visited, adj, dfs)
        return dfs