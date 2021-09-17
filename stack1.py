class Stack:
    def __init__(self):
        self.stack=[]  

    def push(self,val):
        self.stack.append(val)

    def pop(self):

        if len(self.stack) <= 0 :
            return "Stack underflow!!"
        
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]   #[1,2,3]


      
stackObj1 = Stack()

stackObj1.push(1)
stackObj1.push(2)
stackObj1.push(3)
stackObj1.push(4)

print(stackObj1.stack)

stackObj2 = Stack()

stackObj2.push('a')
stackObj2.push('b')
stackObj2.push('c')
stackObj2.push('d')

print(stackObj2.stack)