class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=nums
        self.k=k
        
        length=len(self.heap)
        for i in range(length//2, -1, -1):
            self.heap=self.heapify(heap=self.heap, i=i)
        
        while len(self.heap)>self.k:
            self.heapPop()
    
    def add(self, val: int) -> int:
        self.heapPush(val)
        
        while len(self.heap)>self.k:
            self.heapPop()
        return self.heap[0]
        
    def heapify(self, heap, i=0, mode="min"):
        length=len(heap)
        target=i
        left=(2*i)+1
        right=(2*i)+2
        if left<length:
            if mode=="min" and heap[left]<heap[target] or mode=="max" and heap[left]>heap[target]:
                target=left
        if right<length:
            if mode=="min" and heap[right]<heap[target] or mode=="max" and heap[right]>heap[target]:
                target=right
        if target!=i:
            heap[target], heap[i]=heap[i], heap[target]
            heap=self.heapify(heap=heap, i=target, mode=mode)
        return heap
    
    def heapPush(self, val):
        self.heap.append(val)
        i=len(self.heap)-1
        while i>=0:
            self.heap=self.heapify(heap=self.heap, i=i)
            i=(i-1)//2
            
    def heapPop(self):
        last=len(self.heap)-1
        self.heap[last], self.heap[0]=self.heap[0], self.heap[last]
        popped=self.heap.pop()
        self.heap=self.heapify(heap=self.heap)
        return popped
        
            

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
