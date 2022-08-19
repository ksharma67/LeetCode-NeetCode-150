class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        
        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                maxArea = max(maxArea, (index - i) * h)
                start =i
            stack.append((start, height))
        
        for index, height in stack:
            maxArea = max(maxArea, (len(heights) - index) * height)
        
        return maxArea
