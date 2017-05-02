graph = { 1: [2, 3],
          2: [1, 3, 4, 5],
          3: [1, 2, 4],
          4: [2, 3, 5],
          5: [2, 4] }

def isConnected(graph, a, b):
    def testConnected(front, seen):
        print(front, seen)
        if b in front:
            return True
        elif not front:
            return False;
        else:
            return testConnected(
                {x for n in front
                    for x in graph[n]
                        if x not in front|seen},
                front|seen
            )
    return testConnected(set([a]), set())

print('isConnected(1, 5):', isConnected(graph, 1, 5))

