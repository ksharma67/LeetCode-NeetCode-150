class Solution:
	def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
		graph = defaultdict(list)

		for a, b, time in times:
			graph[a].append((b, time))

		dist = [inf for _ in range(n+1)]
		dist[k] = 0

		heap = [(0, k)]


		while heap:
			cost, node = heappop(heap)

			for nei, nei_cost in graph[node]:

				if cost + nei_cost < dist[nei]:
					dist[nei] = cost + nei_cost
					heappush(heap, (dist[nei], nei))

		max_val = max(dist[1:])

		if max_val != inf:
			return max_val
		else:
			return -1
