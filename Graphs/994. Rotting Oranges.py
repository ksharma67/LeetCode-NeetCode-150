class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        nextQueue = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
        minutes = 0
        while queue:
            while queue:
                r, c = queue.pop(0)
                if c-1 >= 0 and grid[r][c-1] == 1:
                    nextQueue.append((r, c-1))
                    grid[r][c-1] = 2
                if r-1 >= 0 and grid[r-1][c] == 1:
                    nextQueue.append((r-1, c))
                    grid[r-1][c] = 2
                if c+1 < n and grid[r][c+1] == 1:
                    nextQueue.append((r, c+1))
                    grid[r][c+1] = 2
                if r+1 < m and grid[r+1][c] == 1:
                    nextQueue.append((r+1, c))
                    grid[r+1][c] = 2
            if nextQueue:
                minutes += 1
            queue = nextQueue
            nextQueue = []
        for i in range(m):
            if 1 in grid[i]:
                return -1
        return minutes
