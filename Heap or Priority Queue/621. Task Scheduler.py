import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = {}
        max_heap = []
        queue = collections.deque()
        time_count = 0
        
        # map the task with number of time it appears
        for task in tasks:
            if task not in task_count:
                task_count[task] = 1
            else:
                task_count[task] += 1
        
        # populate the max-heap, note, we don't care about the name of the task since the problem doesn't ask for it
        for task in task_count:
            heapq.heappush(max_heap, -task_count[task])
        
        # while there are tasks to be process in heap or queue
        while max_heap or queue:
            time_count += 1
            
            # if there is a task that is ready to be use
            if max_heap:
                # get the task with the greatest count. 
				# Note: we just get the count, not really the task it self since we only care about the updating of time_count at the end
                count = heapq.heappop(max_heap) 
				
                # since we store the count as negative in the max-heap, we convert it back to positive, then deduct it with 1 indicating we just used it once
                count = -count - 1 
                
                # if there are still task to be done, we append it to the queue with the time we need to wait
                if count:
                    queue.append((count, time_count + n))
            
            # if the queue is not empty and the queue's front-element's wait time is legit with the current time, we consider it as "ready" and push to the heap
            if queue and queue[0][1] == time_count:
                heapq.heappush(max_heap, -queue.popleft()[0])
                
        return time_count
    
    # TC: O(mlogm + n): Populate Hashmap - O(m); Populate Heap - O(mlogm); Process between max-heap and queue - O(mlogm + n) with m is the number of task
    # SC: O(m): Storage for the hashmap and the heap
