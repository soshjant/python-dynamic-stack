class stack:
    def __init__(self, size=10):
        self.size = size
        self.list = [None] * size
        self.top = -1
        self.log = []

    def push(self, x):
        if self.top >= self.size - 1:
            print('stack is full')
            self.new_size(self.size * 2)
            print('the list has been resized')
        self.top = self.top + 1
        self.list[self.top] = x
        self.log.append(f'push: {x}')

    def pop(self):
        if self.top == -1:
            self.log.append('pop failed: stack is empty')
            print('stack is empty')
            return
        itm = self.list[self.top]
        self.top = self.top - 1
        self.log.append(f'pop: {itm}')
        return itm

    def peak(self):
        if self.top == -1:
            self.log.append('peak failed: stack is empty')
            print('stack is empty')
            return
        self.log.append(f'peak: {self.list[self.top]}')
        return self.list[self.top]

    def new_size(self, size2):
        list2 = [None] * size2
        for i in range(self.top + 1):
            list2[i] = self.list[i]
        self.log.append(f'resize: {self.size} -> {size2}')
        self.size = size2
        self.list = list2

    def show_log(self):
        self.log.append('show_log called')
        last = self.log[-5:]
        return last

    def show_size_top(self):
        self.log.append('show_size_top called')
        return self.top + 1, (self.size - self.top - 1)

    def is_empty(self):
        self.log.append('is_empty called')
        return self.top == -1

    def __len__(self):
        self.log.append('len called')
        return self.top + 1
