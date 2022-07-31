from heapq import *
class MedianFinder:

    def __init__(self):
        self.minHeap = [] # for large sets
        self.maxHeap = [] # for small sets

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -1*num)
        
        if self.minHeap and self.maxHeap and -1*self.maxHeap[0] > self.minHeap[0]:
            val = -1*heappop(self.maxHeap)
            heappush(self.minHeap, val)

        if len(self.maxHeap) > 1 + len(self.minHeap):
            val = -1*heappop(self.maxHeap)
            heappush(self.minHeap, val)
        
        if len(self.maxHeap) + 1 < len(self.minHeap):
            val = heappop(self.minHeap)
            heappush(self.maxHeap, -1*val)
            
    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -1*self.maxHeap[0]
        
        elif len(self.maxHeap) < len(self.minHeap):
            return self.minHeap[0]
        
        else:
            return (-1*self.maxHeap[0] + self.minHeap[0])/2 
