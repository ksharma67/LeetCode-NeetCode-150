class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2 ** 31 - 1
        ROWS, COLS = len(rooms),len(rooms[0])
        q = collections.deque()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        # put every gate into the queue
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r,c))
        # starting from the gate, we found the closest distance bewteen empty room to gate
        # similar to problem Rotten Orange
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                for d in directions:
                    row,col = r + d[0], c + d[1]
                    if (row < 0 or row == ROWS or col < 0 or col == COLS 
                        or rooms[row][col] != INF):
                        continue
                    q.append((row,col))
                    rooms[row][col] = rooms[r][c] + 1  
  
