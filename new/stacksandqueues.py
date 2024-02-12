# Understand the concepts of stacks (Last In, First Out) and queues (First In, First Out).
# Learn how to implement stacks and queues using arrays or linked lists.
# Study common operations like push, pop, enqueue, and dequeue.
# stack:Push: Adds an element to the top of the stack.
# Pop: Removes the element from the top of the stack.
# Peek (optional): Retrieves the element from the top without removing it.
# Que:Enqueue: Adds an element to the rear of the queue.
# Dequeue: Removes the element from the front of the queue.
# Front (optional): Retrieves the element from the front without removing it.

class Stack:
    def __init__(self):
        self.item=[]
    def push(self,data):
        self.item.append(data)
    def is_empty(self):
        return len(self.item)==0
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
    def check_balance(self,expression):
        stack=[]
        for i in expression:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if i==')' and stack[-1]=='(' or i==']' and stack[-1]=='[' or i=='}' and stack[-1]=='{':
                    print('True')
                else:
                    return False

stack=Stack()
print(stack.check_balance("({[]})"))  # Expected output: True
print(stack.check_balance("({[})"))