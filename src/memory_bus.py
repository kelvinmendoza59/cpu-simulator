class MemoryBus:
    def __init__(self):
        self.data = {}

    def read(self, address):
        return self.data.get(address, 0)

    def write(self, address, value):
        self.data[address] = value