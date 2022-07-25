from collections import deque
class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def dfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.pop()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                    c in range(cols) and
                    grid[r][c] == "1" and
                    (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1
        return islands
      
      
      
      
      
      
      

#dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            
            if i<0 or j<0 or i>=row or j>=col or grid[i][j]=="0":
                return
            grid[i][j]="0"
            
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        
        
        row=len(grid)
        col=len(grid[0])
        res=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    dfs(i,j)
                    res+=1
                
        return res
