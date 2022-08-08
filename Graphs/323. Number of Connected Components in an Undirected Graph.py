class Solution:
    count = 0
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        self.count = n
                
        def find(i):
            if parents[i] != i:
                parents[i] = find(parents[i])
            return parents[i]
            
        def union(i, j):
            rootI = find(i)
            rootJ = find(j)
            if rootI != rootJ:
                parents[rootJ] =  rootI
                self.count -= 1
        
        for edge in edges:
            union(edge[0], edge[1])
            
        return self.count
