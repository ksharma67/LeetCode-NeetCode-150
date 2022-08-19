class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
    # for a valid tree number of edges should be vertices minus one
        if n - 1 != len(edges):
            return False
    # if numbers are right, second thing is to see if there is one tree or several trees with circles
  
        graph = [[] for i in range(n)]
        visited = [0] * n
        self.count = 0  
    
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(graph, visited, i):
            if visited[i]: 
                return  
            visited[i] = 1
            self.count += 1    
            for j in graph[i]:
                dfs(graph, visited, j)                
    # start with one point(any point), traverse, record the number of vertices, if it turns out to be n
    # that means there is only one valid tree 
        dfs(graph, visited, 0)
        return self.count == n  
