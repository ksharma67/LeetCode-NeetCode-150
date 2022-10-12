class TimeMap:

	def __init__(self):
		# timemap with keys as keys and the list of timestamps and values as the values
		self.timeMap = defaultdict(list)

	def set(self, key: str, value: str, timestamp: int) -> None:
		# append to array in time map
		self.timeMap[key].append((timestamp, value)) 

	def get(self, key: str, timestamp: int) -> str:
		# get array from results from the key
		keyValues = self.timeMap[key]
		# if nothing in it we can just return ""
		if len(keyValues) == 0: return ""

		# binary search on array
		l, r = 0, len(keyValues)-1

		while l+1 < r:
			mid = (l+r)//2
			if keyValues[mid][0] == timestamp:
				return keyValues[mid][1]
			elif keyValues[mid][0] < timestamp:
				l = mid
			else:
				r = mid - 1

		# if the timestamp at right pointer is greater than left and <= timestamp, set l to r 
		l = r if (keyValues[r][0] > keyValues[l][0] and keyValues[r][0] <= timestamp) else l

		# return value at l idx if the timestamp is <= timestamp else "" 
		return keyValues[l][1] if keyValues[l][0] <= timestamp else "" 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
