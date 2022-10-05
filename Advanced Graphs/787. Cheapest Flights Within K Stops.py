import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for s, d, w in flights:
            adj_matrix[s][d] = w
        distances = [float("inf") for _ in range(n)]
        current_stops = [float("inf") for _ in range(n)]
        distances[src], current_stops[src] = 0, 0
        minHeap = [(0, 0, src)]     
        while minHeap:       
            cost, stops, node = heapq.heappop(minHeap)
            
            # If destination is reached, return the cost to get here
            if node == dst:
                return cost
            
            # If there are no more steps left, continue 
            if stops == K + 1:
                continue
             
            # Examine and relax all neighboring edges if possible 
            for nei in range(n):
                if adj_matrix[node][nei] > 0:
                    dU, dV, wUV = cost, distances[nei], adj_matrix[node][nei]
                    
                    # Better cost?
                    if dU + wUV < dV:
                        distances[nei] = dU + wUV
                        heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))
                    elif stops < current_stops[nei]:
                        #  Better steps?
                        heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))
                        
                    current_stops[nei] = stops
            
        return -1 if distances[dst] == float("inf") else distances[dst]
