class RingBuffer:

    def __init__(self, capacity):
        ## has a set size that cannot be increased, so:
        self.capacity = capacity
        self.buffer = []
    
    class FullBuffer:
        def __init__(self, capacity):
            self.capacity = capacity
            self.buffer = []
            self.current = 0
        def append(self, item):
            self.buffer[self.current] = item
            self.current = (self.current + 1) % self.capacity
        def get(self):
            return self.buffer[self.current:] + self.buffer[:self.current]

    def append(self, item):
        self.buffer.append(item)
        if len(self.buffer) == self.capacity:
            self.current = 0
            self.__class__ = self.FullBuffer

    def get(self):
        return self.buffer
