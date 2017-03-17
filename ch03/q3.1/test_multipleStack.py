class MultiStack:
    def __init__(self, stackCount, stackSize):
        self.stackSize = stackSize
        self.stackCount = stackCount
        self.pool = [None] * (stackCount * stackSize)
        self.heads = []
        for i in range(stackCount):
            self.heads.append(stackSize * i - 1)

    def push(self, stack, data):
        if self.heads[stack] < self.stackSize * (stack + 1):
            self.heads[stack] += 1
            self.pool[self.heads[stack]] = data
        else:
            raise BufferError

    def pop(self, stack):
        if self.heads[stack] >= self.stackSize * stack:
            data = self.pool[self.heads[stack]]
            self.pool[self.heads[stack]] = None
            self.heads[stack] -= 1
            return data
        else:
            raise None

    def peek(self, stack):
        if self.heads[stack] >= self.stackSize * stack:
            return self.pool[self.heads[stack]]
        else:
            raise None

    def isEmpty(self, stack):
        return self.heads[stack] < self.stackSize * stack


def test_multiStack():
    l = [[] for _ in range(3)]
    for i in range(3):
        l[i].extend(range(6*i, 6*(i+1)))
    ms = MultiStack(3, 6)
    for i in range(3):
        for d in l[i]:
            ms.push(i, d)
    for i in range(3):
        poped = []
        while not ms.isEmpty(i):
            poped.append(ms.pop(i))
        assert poped == l[i][::-1]

