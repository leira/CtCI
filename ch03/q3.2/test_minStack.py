class MinStack:
    def __init__(self):
        self.stack = []
        self.minIndics = []

    def push(self, data):
        pytest.set_trace()
        if len(self.minIndics) == 0:
            self.minIndics.append(len(self.stack))
        else:
            min = self.stack[self.minIndics[-1]]
            if data < min:
                self.minIndics.append(len(self.stack))
            else:
                self.minIndics.append(self.minIndics[-1])
        self.stack.append(data)

    def pop(self):
        self.minIndics.pop()
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def min(self):
        if len(self.minIndics) == 0:
            return None
        else:
            return self.stack[self.minIndics[-1]]


def test_minStack():
    l = [12, 8, 11, 9, 5, 7, 6, 1, 3]
    m = [12, 8, 8, 8, 5, 5, 5, 1, 1][::-1]
    ms = MinStack()
    for d in l:
        ms.push(d)
    mm = []
    while not ms.isEmpty():
        mm.append(ms.min())
        ms.pop()
    assert mm == m

