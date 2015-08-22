__author__ = 'raihan'

#from Node import Node


class Stack:

    def __init__(self):
        self.top = None
        self.stack = []
        self.min = 1000000
        self.__min2 = 1000000

    def push(self, item):
        if item < self.min:
            self.__min2 = self.min
            self.min = item
        self.stack.append(item)

    def pop(self):
        if self.peek() == self.min:
            self.min = self.__min2
            self.__min2 = 1000000
        self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack)-1]

    #@property
    def is_empty(self):
        return len(self.stack) == 0

    def min(self):
        return self.min

#test code
'''
st = Stack()
fv = Node(5, None, None)
sx = Node(6, None, None)
sv = Node(7, None, None)

st.push(fv)
st.push(sx)
st.push(sv)

print(st.peek().value)
st.pop()
print(st.peek().value)
'''
stack = Stack()
stack.push(3)
print(stack.min)

stack.push(5)
print(stack.min)

stack.push(1)
print(stack.min)

stack.pop()
print(stack.min)
