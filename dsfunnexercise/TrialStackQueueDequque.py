# Implement a Stack
# It should have the methods:
# Check if its empty
# Push a new item
# Pop an item
# Peek at the top item
# Return the size

class TrialStack(object):

    def __init__(self):
        self.elements = []

    def isempty(self):
        return self.elements == []

    def push(self, ele):
        self.elements.append(ele)

    def pop(self):
        return self.elements.pop()

    def peek(self):
        return self.elements[len(self.elements) - 1]

    def size(self):
        return len(self.elements)


s = TrialStack()
print(s.isempty())
s.push(5)
print(s.peek())
print(s.size())
print(s.isempty())
print(s.pop())


# Implementation of Queue
# Queue Methods and Attributes
# Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
# enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
# dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
# isEmpty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
# size() returns the number of items in the queue. It needs no parameters and returns an integer.

class TrialQueue(object):
    def __init__(self):
        self.elements = []

    def isempty(self):
        return self.elements == []

    def enqueue(self, ele):
        self.elements.insert(0, ele)

    def dequeue(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)


q = TrialQueue()
print(q.isempty())
q.enqueue(5)
print(q.size())
print(q.isempty())
print(q.dequeue())


# Implement a Deque
#  Check if its empty
#  Add to both front and rear
# Remove from Front and Rear
# Check the Size

class TrialDeque(object):
    def __init__(self):
        self.elements = []

    def isempty(self):
        return self.elements == []

    def addfront(self, ele):
        self.elements.insert(0, ele)

    def addrear(self, ele):
        self.elements.append(ele)

    def removefront(self):
        return self.elements.pop()

    def removerear(self):
        return self.elements.pop(0)

    def size(self):
        return len(self.elements)


d = TrialDeque()
print(d.isempty())
d.addfront('hello')
d.addrear('world')
print(d.size())
print(d.isempty())
print(d.removefront() + ' ' + d.removerear())
print(d.size())
