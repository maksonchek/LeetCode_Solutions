class RecentCounter:

    def __init__(self):
        self.pings = {}
        self.id = 0
        self.id_cntr = 0

    def ping(self, t: int) -> int:
        self.pings[self.id_cntr] = t
        self.id_cntr += 1
        while t - 3000 > self.pings[self.id]:
            del self.pings[self.id]
            self.id += 1
        return len(self.pings)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)