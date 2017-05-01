graph = { 1: set([2, 3]),
          2: set([1, 3, 4, 5]),
          3: set([1, 2, 4]),
          4: set([2, 3, 5]),
          5: set([2, 4]) }

def isConnected(graph, a, b):
    front = set([a,])
    seen = set()
    while len(front):
        if b in front:
            return True;
        seen |= front
        front = { x for n in front for x in graph[n] if x not in seen }
        print('front:', front)
        print('seen:', seen)
    return False

print('isConnected(1, 5):', isConnected(graph, 1, 5))

