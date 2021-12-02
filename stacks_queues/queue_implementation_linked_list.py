"""
Queues are another form of linear data structure very similar to stacks.
The difference is queues follow the FIFO rule - First In First Out, much like real life queues,
Where the person gets in first, gets to leave first.
Queues can be implemented with both arrays and linked lists but the array implementation is not efficient
Because for removing an element from the queues, which happens from the front of the array(queue),
the indices of the array have to be updated every time, essentially making it an O(n) operation,
Whereas the same operation can be done in O(1) time with linked lists.
Queues have enqueue and dequeue operations which correspond to the push and pop operations of stacks ,
only difference being dequeue removes element from the front
Time complexities are as follows:

Lookup                              -   O(n)
Peek (Retrieve the top element)     -   O(1)
Enqueue (Push at the end)           -   O(1)
Dequeue (Pop from the front)        -   O(1)

"""

class Node:
    """
    Linked Lists are made of nodes. So we create a node class.
    It will contain the data and the pointer to the next node.
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """
    Implementation a queue using linked lists
    """
    def __init__(self):
        """
        The 'first' pointer will always point to the front of the queue
        (the element which is to be removed next that is)
        The 'last' pointer will always point to the end of the queue
        (the element which has last been entered)
        """
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        """
        Return the element at the front of the queue
        :return: he element at the front of the queue
        """
        if self.first:
            return self.first.value
        else:
            return None

    def enqueue(self, value):
        """
        Add an element at the end of the queue.
        If the queue is empty, both the first and last pointer point to the new node
        Else, it will first make the next of the new node to point to the present last node
        and then it will update the last node to point to the new node
        Time complexity will be O(1)
        :param value: element to add
        :return:
        """
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        """
        Remove the front element of the queue
        #If the queue is empty, it will print an appropriate message
        #Else, it will simply make the first pointer point to the next element of the first pointer.
        :return:
        """
        pop_node = self.first
        if not pop_node:
            # If the queue is empty, we print an appropriate message
            print("Queue is empty")
            return None
        # We make the last pointer None if there was only 1 element in the queue and that gets popped
        if self.last == self.first:
            self.last = None
        # Make the first pointer point to the next of the first pointer and decrease the length by 1,
        # effectively deleting the top element.
        self.first = self.first.next
        self.length -= 1
        return pop_node

    def is_empty(self):
        """
        Check if queue is empty or not
        :return:
        """
        if self.length == 0:
            return True
        return False

    def print_queue(self):
        """
        which prints the elements of the queue in, well, a queue like format
        This will be an O(n) operation
        as we'll obviously have to traverse the entire linked list to print all elements
        :return:
        """
        if self.is_empty():
            print("[Queue is empty]")
        else:
            cur_node = self.first
            print("[", end="")
            while cur_node:
                if cur_node.next is None:
                    print(cur_node.value, end="")
                else:
                    print(f"{cur_node.value} <-- ", end="")
                cur_node = cur_node.next
            print("]")


if __name__ == "__main__":
    # create
    my_queue = Queue()
    my_queue.print_queue()
    print("peek = ", my_queue.peek())
    my_queue.print_queue()
    # enqueue
    my_queue.enqueue("Joy")
    print("peek = ", my_queue.peek())
    my_queue.print_queue()
    #
    my_queue.enqueue("Matt")
    print("peek = ", my_queue.peek())
    my_queue.print_queue()
    #
    my_queue.enqueue("Pavel")
    print("peek = ", my_queue.peek())
    my_queue.print_queue()
    #
    my_queue.enqueue("Samir")
    print("peek = ", my_queue.peek())
    my_queue.print_queue()
    # dequeue
    node = my_queue.dequeue()
    print("dequeue = ", node.value)
    print("peek = ", my_queue.peek())
    my_queue.print_queue()
    #
    node = my_queue.dequeue()
    print("dequeue = ", node.value)
    print("peek = ", my_queue.peek())
    my_queue.print_queue()
    #
    node = my_queue.dequeue()
    print("dequeue = ", node.value)
    print("peek = ", my_queue.peek())
    my_queue.print_queue()
    #
    node = my_queue.dequeue()
    print("dequeue = ", node.value)
    print("peek = ", my_queue.peek())
    my_queue.print_queue()
