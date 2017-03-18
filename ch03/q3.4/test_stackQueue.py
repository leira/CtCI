class StackQueue:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def add(self, data):
        self.inStack.append(data)

    def remove(self):
        if not self.outStack:
            self.__pushToOut()
        return self.outStack.pop()

    def peek(self):
        if not self.outStack:
            self.__pushToOut()
        return self.outStack[-1]

    def isEmpty(self):
        return not self.inStack and not self.outStack

    def __pushToOut(self):
        while self.inStack:
            self.outStack.append(self.inStack.pop())

def test_StackQueue():
    q = StackQueue()
    q.add(0)
    q.add(1)
    assert q.remove() == 0
    q.add(2)
    q.add(3)
    q.remove()
    assert q.remove() == 2

