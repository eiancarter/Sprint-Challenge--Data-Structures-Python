class RingBuffer:
    def __init__(self, capacity):
        ## has a set size that cannot be increased, so:
        self.capacity = capacity
        self.buffer = []

    def append(self, item):
        self.buffer.append(item)
        if len(self.buffer) == self.capacity:
            self.current = 0

    def get(self):
        return self.buffer