class Queue:
    # first in first out
    def __init__(self):
        self.item=[]
    def is_empty(self):
        return len(self.item)==0
    def enqueue(self, items): 
        # additem
        self.item.append(items)
    def dequeue(self):
        # deleteitem
        if not self.is_empty():
            return self.item.pop(0) 
        # pop the first on out

queue=Queue()
# Check if Queue is Empty
print("Is Queue Empty?", queue.is_empty())  # Should be True

# Enqueue Elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Check Queue Size
print("Queue Size:", len(queue.item))  # Should be 3

# Dequeue Element
dequeued_item = queue.dequeue()
print("Dequeued Element:", dequeued_item)  # Should be 1

# Check Updated Queue
print("Updated Queue:", queue.item)  # Should be [2, 3]