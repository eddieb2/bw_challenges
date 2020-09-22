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
        # NOTES:
        # Pop all items off of s1 until we reach the first element,
        # push all popped elements from s1 to s2,
        # store and remove the first element
        # pop all items off s2 and push them to s1, giving us the original stack
        # return removed element

        while (self.s1.__len__() > 1):
            # self.s2.print_s()
            self.s2.push(self.s1.pop())

        removed = self.s1.pop()

        while (self.s2.__len__() != 0):
            # self.s1.print_s()
            self.s1.push(self.s2.pop())

        return removed

    def peek(self) -> int:
        """
        Get the front element.
        """
        # NOTES:
        # Pop all items off of s1 until we reach the first element,
        # push all popped elements from s1 to s2,
        # store element to print,
        # pop all items off s2 and push them to s1, giving us the original stack
        # return element to print
        while (self.s1.__len__() > 1):
            # self.s2.print_s(
            self.s2.push(self.s1.pop())

        first_element = self.s1.storage[0]

        while (self.s2.__len__() != 0):
            # self.s1.print_s()
            self.s1.push(self.s2.pop())

        return first_element

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.s1.__len__() == 0:
            return True
        else:
            return False