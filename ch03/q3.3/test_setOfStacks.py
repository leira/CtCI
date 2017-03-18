class SetOfStacks:
    def __init__(self, stackSize):
        self.stackSize = stackSize
        self.stacks = []

    def isEmpty(self):
        return len(self.stacks) == 0

    def push(self, data):
        if len(self.stacks) == 0 \
        or len(self.stacks[-1]) >= self.stackSize:
            self.stacks.append([])
        self.stacks[-1].append(data)

    def pop(self):
        if self.isEmpty():
            raise IndexError
        data = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return data

    def peek(self):
        if self.isEmpty():
            raise IndexError
        return self.stacks[-1][-1]

    def popAt(self, index):
        if len(self.stacks) <= index:
            raise IndexError
        data = self.stacks[index].pop()
        if len(self.stacks[index]) == 0:
            del self.stacks[index]
        return data


def test_setOfStacks():
    sos = SetOfStacks(6)
    for i in range(19):
        sos.push(i)
    assert sos.popAt(2) == 17
    assert sos.pop() == 18

    for i in range(16, -1, -1):
        assert sos.pop() == i

