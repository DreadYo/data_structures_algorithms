"""
Queue Implementation using Stacks (Leetcode 232)
Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue
(push, peek, pop, and empty).

Implement the MyQueue class:
- void push(int x)      Pushes element x to the back of the queue.
- int pop()             Removes the element from the front of the queue and returns it.
- int peek()            Returns the element at the front of the queue.
- boolean empty()       Returns true if the queue is empty, false otherwise.

Notes:
- You must use only standard operations of a stack,
which means only push to top, peek/pop from top, size, and is empty operations are valid.
- Depending on your language, the stack may not be supported natively.
You may simulate a stack using a list or deque (double-ended queue)
as long as you use only a stack's standard operations.

Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false


Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity?
In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

--------------------------------------

This ia popular interview question. Implementation of a queue using stacks.
We have access to stacks push and pop operations.
Using those we need to execute a qeueue's enqueue and dequeue operation

I'll do it using my class Stack implementation using arrays

I have 2 stacks: stack1 and stack2. And var front: the first element in queue

Push:
I store queue in stack1.
if stack1 is empty, I push new element in stack1 and and var front assign to new element.
If stack1 is not empty, I pop all elements one by one from stack1 to stack2.
Then I push new element in stack1.
And I pop all elements one by one from stack2 to stack1.

Pop:
If stack1 is not empty, pop element from stack1
And front assign to stack1.peek()

Peek:
return front

Time complexity:
Peek (Retrieve the top element)     -   O(1)
Enqueue (Push at the end)           -   O(n)
Dequeue (Pop from the front)        -   O(1)

Space complexity:
Peek (Retrieve the top element)     -   O(1)
Enqueue (Push at the end)           -   O(n)
Dequeue (Pop from the front)        -   O(1)

"""

from stacks_queues.stack_implementation_array import Stack


class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.front = None

    def push(self, x: int) -> None:
        print(f"push: {x}")
        # check input
        if not x:
            print("input is invalid")
        else:
            if self.stack1.is_empty():
                self.front = x
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
            self.stack1.push(x)
            while not self.stack2.is_empty():
                self.stack1.push(self.stack2.pop())

    def pop(self) -> int:
        print("pop")
        pop_el = None
        if not self.stack1.is_empty():
            pop_el = self.stack1.pop()
            self.front = self.stack1.peek()
        return pop_el

    def peek(self) -> int:
        print("peek")
        return self.front

    def empty(self) -> bool:
        return self.stack1.is_empty()

    def print_queue(self):
        """
        Print stack1 for check
        :return:
        """
        if self.empty():
            print("[Queue is empty]")
        else:
            self.stack1.print_stack()


if __name__ == "__main__":
    # create
    my_queue = MyQueue()
    my_queue.print_queue()
    # push
    my_queue.push("1")
    my_queue.print_queue()
    my_queue.push("2")
    my_queue.print_queue()
    my_queue.push("3")
    my_queue.print_queue()
    # peek
    print(my_queue.peek())
    # pop
    param_1 = my_queue.pop()
    print(param_1)
    # peek
    print(my_queue.peek())
    # pop
    my_queue.print_queue()
    param_2 = my_queue.pop()
    print(param_2)
    my_queue.print_queue()
    # pop
    param_3 = my_queue.pop()
    print(param_3)
    my_queue.print_queue()

    print(my_queue.peek())


