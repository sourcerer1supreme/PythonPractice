from typing import Deque


class Queue:

    def __init__(self):
        self.queue = []
        self.rear = -1
        self.front = 0
        
    def enqueue(self,val):
        self.queue.append(val)
        self.rear+=1

    def dequeue(self):
        if(self.front>self.rear):
            return "queue underflow!"
        
        self.front+=1
        return self.queue.pop(0)
    
    
    def queueStatus(self):
        print(f'Current position of FRONT and REAR are: {self.front} and {self.rear}')


q1 = Queue()
q2 = Queue()

q1.enqueue('apple')
q1.enqueue('grapes')
q1.enqueue('pear')
q1.enqueue('guava')

print(q1.queue)

print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())