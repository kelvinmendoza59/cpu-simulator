class Cache:
    def __init__(self):
        self.enabled = False
        self.cache = {}

    def read(self, address, memory_bus):
        if not self.enabled:
            return memory_bus.read(address)
        if address in self.cache:
            print(f"Cache hit for address {address}")
            return self.cache[address]
        else:
            print(f"Cache miss for address {address}")
            data = memory_bus.read(address)
            self.cache[address] = data
            return data

    def write(self, address, data, memory_bus):
        if self.enabled:
            self.cache[address] = data
        memory_bus.write(address, data)

    def flush(self):
        self.cache.clear()

    def turn_on(self):
        self.enabled = True

    def turn_off(self):
        self.enabled = False