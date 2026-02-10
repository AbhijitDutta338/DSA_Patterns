class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.frequencies = defaultdict(OrderedDict)
        self.minf = 0
        self.capacity = capacity
    def insert(self, key, frequency, value):
        self.cache[key] = (frequency, value)
        self.frequencies[frequency][key] = value
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        frequency, value = self.cache[key]
        del self.frequencies[frequency][key]
        if not self.frequencies[frequency]:
            del self.frequencies[frequency]
            if frequency == self.minf:
                self.minf += 1
        self.insert(key, frequency + 1, value)
        return value
    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.cache:
            frequency = self.cache[key][0]
            self.cache[key] = (frequency, value)
            self.get(key)
            return
        if self.capacity == len(self.cache):
            key_to_delete, frequency = self.frequencies[self.minf].popitem(last=False)
            del self.cache[key_to_delete]
        self.minf = 1
        self.insert(key, 1, value)