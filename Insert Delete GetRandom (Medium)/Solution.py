class RandomizedSet:

    def __init__(self):
        self.rdict = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.rdict:
            return False
        self.rdict[val] = len(self.data)
        self.data.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.rdict:
            return False
        last = self.data[-1]
        r_id = self.rdict[val]

        self.rdict[last] = r_id
        self.data[r_id] = last
        self.data.pop()
        self.rdict.pop(val)
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.data)
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()