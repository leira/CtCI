import pytest

class Animal:
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.timestamp = 0

class AnimalShelter:
    def __init__(self):
        self.currentTime = 0
        self.animalQeues = {}

    def enqueue(self, animal):
        animal.timestamp = self.currentTime
        self.currentTime += 1
        queue = self.animalQeues.setdefault(animal.type, [])
        queue.append(animal)

    def dequeue(self, type):
        try:
            queue = self.animalQeues[type]
            animal = queue.pop(0)
            if not queue:
                del self.animalQeues[type]
            return animal
        except KeyError:
            raise IndexError

    def dequeueAny(self):
        try:
            type, queue = min(self.animalQeues.items(),
                         key = lambda i: i[1][0].timestamp)
            return self.dequeue(type)
        except ValueError:
            raise IndexError


@pytest.fixture
def shelter():
    sht = AnimalShelter()
    sht.enqueue(Animal('cat', 'c1'))
    sht.enqueue(Animal('cat', 'c2'))
    sht.enqueue(Animal('dog', 'd1'))
    sht.enqueue(Animal('dog', 'd2'))
    sht.enqueue(Animal('cat', 'c3'))
    sht.enqueue(Animal('dog', 'd3'))
    sht.enqueue(Animal('cat', 'c4'))
    sht.enqueue(Animal('dog', 'd4'))
    return sht

def test_empty():
    emptyS = AnimalShelter()
    with pytest.raises(IndexError):
        emptyS.dequeueAny()
    with pytest.raises(IndexError):
        emptyS.dequeue('cat')

def test_dequeueAny(shelter):
    animals = ['c1', 'c2', 'd1', 'd2', 'c3', 'd3', 'c4', 'd4']
    sh_animals = []
    for i in range(8):
        sh_animals.append(shelter.dequeueAny().name)
    assert sh_animals == animals
    with pytest.raises(IndexError):
        shelter.dequeueAny()

def test_dequeueCat(shelter):
    animals = ['c1', 'c2', 'c3', 'c4']
    sh_animals = []
    for i in range(4):
        sh_animals.append(shelter.dequeue('cat').name)
    assert sh_animals == animals
    with pytest.raises(IndexError):
        shelter.dequeue('cat')

