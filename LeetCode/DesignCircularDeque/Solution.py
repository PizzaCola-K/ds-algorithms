class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.q = [None] * k
        self.maxlen = k
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.q[self.front - 1] is None:
            self.q[self.front - 1] = value
            self.front = (self.front - 1) % self.maxlen
            return True
        else:
            return False        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.maxlen
            return True
        else:
            return False
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.q[self.front] is None:
            return False
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.maxlen
            return True

        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.q[self.rear - 1] is None:
            return False
        else:
            self.q[self.rear - 1] = None
            self.rear = (self.rear - 1) % self.maxlen
            return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return -1 if self.q[self.front] is None else self.q[self.front]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return -1 if self.q[self.rear - 1] is None else self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.rear == self.front and self.q[self.front] is None
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.rear == self.front and self.q[self.front] is not None
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
