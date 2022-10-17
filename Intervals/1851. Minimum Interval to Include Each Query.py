# * Sorting and Priority Queue (Min Heap) Solution | O(nlogn+qlogq) Time | O(n) Space
# * n -> The length of intervals array | q -> The length of queries array


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # * Sort the intervals in ascending order based on the left value.
        intervals.sort(key=lambda interval: interval[0])
        res = {}
        # * Stores a pair of the size and right value of the interval.
        # * Pair -> (size, right_val)
        min_heap = []
        i = 0

        # * Sort the queries in ascending order.
        for query in sorted(queries):
            # * Push the intervals into the min heap that the current query belongs to.
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                heapq.heappush(min_heap, (right - left + 1, right))
                i += 1

            # * Pop the intervals from the min heap that are OOB of the current query.
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            # * Add the smallest interval from the min heap to the current query.
            res[query] = min_heap[0][0] if min_heap else -1

        return [res[query] for query in queries]
