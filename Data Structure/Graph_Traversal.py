class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {vertex: [] for vertex in range(vertices + 1)}

    def addEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def BFS(self, f_vertex):
        visited = [False] * (max(self.graph) + 1)
        que = []

        que.append(f_vertex)
        visited[f_vertex] = True

        while que:

            v = que.pop(0)
            print(v, end=' ')

            for vertex in self.graph[v]:
                if not visited[vertex]:
                    que.append(vertex)
                    visited[vertex] = True

    def DFS(self, f_vertex):
        visited = [False] * (max(self.graph) + 1)
        stk = [f_vertex]

        while stk:
            v = stk.pop()
            print(v, end=' ')
            if not visited[v]:
                visited[v] = True

            for vertex in reversed(self.graph[v]):
                if not visited[vertex]:
                    stk.append(vertex)


graph = Graph(7)
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(2, 4)
graph.addEdge(2, 5)
graph.addEdge(3, 6)
graph.addEdge(3, 7)
graph.BFS(1)      # 1,2,3,4,5,6,7
print('\n')
graph.DFS(1)      # 1,2,4,5,3,6,7

