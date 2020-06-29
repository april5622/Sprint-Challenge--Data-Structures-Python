
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.cur = 0
        
        
    def append(self, item):
        # append the item if the data is less than the capacity
        if len(self.data) < self.capacity:
            self.data.append(item)
        # Append an item overwriting the oldest
        else: 
            self.data[self.cur] = item
            self.cur = (self.cur +1) % self.capacity
 

    def get(self):
        return self.data