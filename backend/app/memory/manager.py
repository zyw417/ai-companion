class MemoryManager:


    def __init__(self):

        self.short_memory = []


    def remember(self, item):

        self.short_memory.append(item)


    def get_memory(self):

        return self.short_memory
