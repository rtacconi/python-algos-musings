from enum import Enum

class QueueType(Enum):
    FIFO = 1
    LIFO = 2

class Queue(object):
    def __init__(self, queue_type):
        self.data = []
        self.queue_type = queue_type

    def push(self, item):
        try:
            self.data.append(item)
            return True
        except MemoryError as error:
            return False

    def pop(self):
        if len(self.data) > 0:
            if self.queue_type == QueueType.FIFO:
                return self.data.pop(0)
            elif self.queue_type == QueueType.LIFO:
                return self.data.pop(-1)
            else:
                raise ValueError
        else:
            return None

q = Queue(QueueType.LIFO)
q.push(1)
q.push(2)
q.push(3)
q.data
q.pop()

result = q.push(1)


if result:
    print("Item inserted")
else:
    print("Memory is full, cannot insert")

result = q.pop()

if result:
    print(result)
else:
    print("The queue is empty")

result = q.pop()

if result:
    print(result)
else:
    print("The queue is empty")
