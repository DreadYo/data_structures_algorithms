"""
Implementation Queue in Python using stacks.
But in this implementation I will not create (using) additional class Stack.
I will use 2 arrays
It's the same solution with amortized O(n) complexity of dequeue
"""


class ShortQueue:
    def __init__(self):
        self.first = []
        self.second = []
        self.front = None

    def enqueue(self, value):
        if len(self.first) == 0:
            self.front = value
        self.first.append(value)

    def dequeue(self):
        if len(self.second) == 0:
            for i in range(len(self.first)):
                self.second.append(self.first.pop())
        return self.second.pop()

    def peek(self):
        if len(self.first) == 0 and len(self.second) == 0:
            self.front = None
        if len(self.second) > 0:
            self.front = self.second[-1]
        return self.front

    def print_queue(self):
        """
        Print arrays for check
        :return:
        """
        print(f"first = {self.first}, second = {self.second}")


if __name__ == "__main__":
    # create
    my_queue = ShortQueue()
    print(f"peek {my_queue.peek()}")
    my_queue.print_queue()
    # enqueue
    print("enqueue Joy")
    my_queue.enqueue('Joy')
    my_queue.print_queue()
    print("enqueue Matt")
    my_queue.enqueue('Matt')
    my_queue.print_queue()
    print("enqueue Pavel")
    my_queue.enqueue('Pavel')
    my_queue.print_queue()

    print(f"peek {my_queue.peek()}")
    # dequeue
    print("dequeue")
    print(my_queue.dequeue())
    my_queue.print_queue()
    print(f"peek {my_queue.peek()}")
    my_queue.print_queue()
    print("dequeue")
    print(my_queue.dequeue())
    my_queue.print_queue()
    print(f"peek {my_queue.peek()}")
    print("dequeue")
    print(my_queue.dequeue())
    my_queue.print_queue()
    #
    print(f"peek {my_queue.peek()}")
