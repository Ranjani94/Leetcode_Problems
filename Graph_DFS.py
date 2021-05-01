

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addgraph(self, u, v):
        self.graph[u].append(v)

    def DFS(self, v):

        visited = set()
        # call recursively to do DFS traversal
        self.dfs(v, visited)

    def dfs(self, v, visited):

        visited.add(v)
        print(v)
        for next_node in self.graph[v]:
            if next_node not in visited:
                self.dfs(next_node, visited)


g = Graph()

g.addgraph(0,1)
g.addgraph(0,2)
g.addgraph(1,2)
g.addgraph(2,0)
g.addgraph(2,3)
g.addgraph(3,3)

g.DFS(2)



