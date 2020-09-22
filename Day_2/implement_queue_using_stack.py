class Stack:
    def __init__(self):
        self.storage = []
    
    def __len__(self):
        return len(self.storage)
    
    def push(self, x):
        return self.storage.append(x)
    
    def pop(self):
        if len(self.storage) != 0:
            return self.storage.pop()
    
    def print_s(self):
        print(self.storage)
    
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = Stack()
        self.s2 = Stack()
        
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.push(x)
        
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # store pop value in s2 from s1 until length of s1 == 1, then pop and return last value in s1
        while(self.s1.__len__() > 1):
            # self.s2.print_s()
            self.s2.push(self.s1.pop())
            
        removed = self.s1.pop()

        while(self.s2.__len__() != 0):
            # self.s1.print_s()
            self.s1.push(self.s2.pop())

        return removed

    def peek(self) -> int:
        """
        Get the front element.
        """
        while (self.s1.__len__() > 1):
            # self.s2.print_s()
            self.s2.push(self.s1.pop())

        return self.s1.storage[0]

        while (self.s2.__len__() != 0):
            # self.s1.print_s()
            self.s1.push(self.s2.pop())

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.s1.__len__() == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.peek()
print(obj.empty())
obj.s1.print_s()


# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()