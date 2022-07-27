class LRUCache:
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
    class Node:
        def __init__(self, key, val, prev, next):
            self.key = key
            self.val = val
            self.prev = prev
            self.next = next
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.root = self.Node(None, None, None, None)
        self.tail = self.Node(None, None, self.root, None)
        self.root.next = self.tail
        self.lookup = {}

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        node = self.lookup[key]
        self._moveToFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.lookup:
            node = self.Node(key, value, None, None)
            self.lookup[key] = self._pushInFront(node)
        else:
            node = self.lookup[key]
            node.val = value
            self._moveToFront(node)
        if len(self.lookup) > self.capacity:
            node = self._popFromEnd()
            self.lookup.pop(node.key)

    def _pop(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def _popFromEnd(self):
        node = self.tail.prev
        return self._pop(node)

    def _pushInFront(self, node):
        node.prev = self.root
        node.next = self.root.next
        self.root.next = node
        node.next.prev = node
        return node

    def _moveToFront(self, node):
        popped = self._pop(node)
        return self._pushInFront(popped)
