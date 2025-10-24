from collections import deque

class ListQueue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0

class DequeQueue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self.items.popleft()
    
    def is_empty(self):
        return len(self.items) == 0

# Test
if __name__ == "__main__":
    # ListQueue
    list_q = ListQueue()
    for i in [10, 20, 30]:
        list_q.enqueue(i)
    print(f"ListQueue: {list(list_q.items)}")
    
    # DequeQueue
    deque_q = DequeQueue()
    for i in [10, 20, 30]:
        deque_q.enqueue(i)
    print(f"DequeQueue: {list(deque_q.items)}")
    
    print(f"Dequeued: {deque_q.dequeue()}")
    print(f"Final: {list(deque_q.items)}")