class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        is_valid = lambda i, j: 0 <= i < n and 0 <= j < m
        drn = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        outgoing = defaultdict(set)
        inDegree = {}
        for i in range(n):
            for j in range(m):
                inDegree[(i, j)] = 0
                for i_drn, j_drn in drn:
                    new_i, new_j = i+i_drn, j+j_drn
                    if is_valid(new_i, new_j):
                        if matrix[i][j] > matrix[new_i][new_j]:
                            inDegree[(i, j)] += 1
                            outgoing[(new_i, new_j)].add((i, j))
        
        queue = deque()
        
        for key in inDegree:
            if inDegree[key] == 0:
                queue.append((key, 1))
        ans = 0
        while queue:
            for _ in range(len(queue)):
                current, ln = queue.popleft()
                ans = max(ans, ln)
                for neigh in outgoing[current]:
                    inDegree[neigh] -= 1
                    if inDegree[neigh] == 0:
                        queue.append((neigh, ln+1))
        return ans
        
