class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        visted = set()
        def dfs(crs):
            if crs in visted:
                return False
            if premap[crs] == []:
                return True   
            visted.add(crs)
            for pre in premap[crs]:
                if not dfs(pre): return False
            visted.remove(crs)
            premap[crs] = []
            return True     
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
