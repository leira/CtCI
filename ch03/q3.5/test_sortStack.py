def sortStack(stack):
    tempStack = []
    while stack:
        data = stack.pop()
        while tempStack and tempStack[-1] > data:
            stack.append(tempStack.pop())
        tempStack.append(data)
    while tempStack:
        stack.append(tempStack.pop())

def test_sortStack():
    import random
    l = [random.randint(0, 100) for _ in range(100)]
    stack = []
    for i in l:
        stack.append(i)
    sortStack(stack)
    for i in sorted(l):
        assert stack.pop() == i

