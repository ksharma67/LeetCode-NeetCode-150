class DetectSquares:

    def __init__(self):
        self.mapp = {}
        
    def add(self, point: List[int]) -> None:
        if tuple(point) not in self.mapp:
            self.mapp[tuple(point)] = 0
        self.mapp[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0 
        px,py = point
        for x,y in self.mapp.keys():
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            if (x,py) in self.mapp and (px,y) in self.mapp:
                res += self.mapp[(x,py)] * self.mapp[(px,y)] * self.mapp[(x,y)]
        return res 
