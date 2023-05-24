# The linked list implementation of a stack can grow and shrink according to the needs at the runtime (ADVANTAGE)
# This implementation requires extra memory due to the involvement of pointers (DISADVANTAGE)
# Random accessing is not possible in this implementation (DISADVANTAGE)

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        print('% d pushed to the stack' % (data))

    def pop(self):
        if self.isEmpty():
            return float('-inf')
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped

    def peek(self):
        if self.isEmpty():
            return float('-inf')
        return self.root.data