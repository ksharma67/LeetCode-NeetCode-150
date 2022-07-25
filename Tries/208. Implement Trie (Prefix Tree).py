def __init__(self):
	self.root = dict()
	self.root[False] = 0

def insert(self, word: str) -> None:
	c = self.root
	for char in word:
		if(char not in c):
			c[char] = dict()
			c[char][False] = 0
		c = c[char]
	c[False] = 1

def search(self, word: str) -> bool:
	c = self.root
	for char in word:
		if(char not in c):
			return False
		c = c[char]
	return c[False]

def startsWith(self, prefix: str) -> bool:
	c = self.root
	for char in prefix:
		if(char not in c):
			return False
		c = c[char]
	return True
