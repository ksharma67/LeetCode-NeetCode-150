class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        for point in points:
            ans.append(point)
            self.heapifyUp(ans, len(ans)-1)
            if len(ans) > k:
                ans[0], ans[-1] = ans[-1], ans[0]
                ans.pop()
                self.heapifyDown(ans, 0)
        return ans
    
    def heapifyDown(self, ans, index):
        if index < len(ans):
            pointDis = ans[index][0]*ans[index][0] + ans[index][1]*ans[index][1]
            leftDis = rightDis = -1
            if index*2 + 1 < len(ans):
                left = ans[index*2 + 1]
                leftDis = left[0]*left[0] + left[1]*left[1]
            if index*2 + 2 < len(ans):
                right = ans[index*2 + 2]
                rightDis = right[0]*right[0] + right[1]*right[1]
            if pointDis < max(leftDis, rightDis):
                if leftDis >= rightDis:
                    ans[index], ans[index*2 + 1] = ans[index*2 + 1], ans[index]
                    self.heapifyDown(ans, index*2 + 1)
                else:
                    ans[index], ans[index*2 + 2] = ans[index*2 + 2], ans[index]
                    self.heapifyDown(ans, index*2 + 2)
            
    def heapifyUp(self, ans, index):
        if index > 0:
            point = ans[index]
            pointDis = point[0]*point[0] + point[1]*point[1]
            parent = ans[(index-1)//2]
            parentDis = parent[0]*parent[0] + parent[1]*parent[1]
            if pointDis > parentDis:
                ans[index], ans[(index-1)//2] = ans[(index-1)//2], ans[index]
                self.heapifyUp(ans, (index-1)//2)
