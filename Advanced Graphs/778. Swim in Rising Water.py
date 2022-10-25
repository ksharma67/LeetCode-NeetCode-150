class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # find the representative of the set
        def parent(x):
            while root[x]!=x:
                root[x]=root[root[x]]
                x=root[x]
            return x

        def union(x,y):
            px=parent(x)
            py=parent(y)
            if px!=py:
                if size[px]>size[py]:
                    px,py=py,px
                size[py]+=size[px]
                root[px]=py

        n=len(grid)
        size=[1]*(n*n)
        root=list(range(n*n))
        vis=[[False]*n for _ in range(n)]
        positions=sorted([(i,j) for i in range(n) for j in range(n)],key=lambda x:grid[x[0]][x[1]])

        for i,j in positions:
            vis[i][j]=True
            # explore the neighbors to grow the disjoint sets
            for x,y in (i+1,j),(i-1,j),(i,j-1),(i,j+1):
                if 0<=x<n and 0<=y<n and vis[x][y]:
                    union(i*n+j,x*n+y)

            # the start and end points are joined together
            if parent(0)==parent(n*n-1):
                return grid[i][j]
