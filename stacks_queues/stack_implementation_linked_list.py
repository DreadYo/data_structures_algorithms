"""
Stacks are linear data-structures which can be implemented using either stacks or linked lists
Insertion and deletion of elements in a stack take place from one end only.
Stacks follow the LIFO rule - Last In First Out,
where the last element that is inserted, is the first element that comes out.
The main operations that can be performed on a stack , with their time complexities are as follows:

Push (Insert)                   -   O(1)
Pop (Remove)                    -   O(1)
Peek (Retrieve the top element) -   O(1)
Lookup                          -   O(n)

"""


class Node:
    """
    Linked Lists are made of nodes. So we create a node class.
    It will contain the data and the pointer to the next node.
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """
    Implementation a stack using linked lists
    """
    def __init__(self):
        """
        Class will consist of a constructor having the top pointer,
        the pointer which points to the top element of the stack at any given time
        The length variable which keeps track of the length of the stack,
        and a bottom pointer which points to bottom most element of the stack
        """
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        """
        The peek method will allow us to peek at the top element,
        It will return the element at the top of the stack without removing it from the stack.
        Since for this we only need to see what the top pointer points at, the time complexity will be O(1)
        :return: the top element
        """
        if self.top:
            return self.top.value
        else:
            return None

    def push(self, value):
        """
        Insert an element at the top of the stack
        Again this only requires access to the top pointer and involves no looping.
        So time complexity is O(1)
        :param value: value to put in the stack
        :return:
        """
        new_node = Node(value)
        # If the stack is empty, we make the top and bottom pointer both point to the new node
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        # Otherwise, we make the next of the new node,
        # which was pointing to None,
        # point to the present top and then update the top pointer
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        """
        Remove the top element from the stack
        Its time complexity is O(1) as well
        :return:
        """
        pop_node = self.top
        # We make the bottom pointer None if there was only 1 element in the stack and that gets popped
        if self.top == self.bottom:
            self.bottom = None
        # Else we make the top pointer point to the next of the top pointer and decrease the length by 1,
        # effectively deleting the top element.
        if pop_node:
            self.top = pop_node.next
            self.length -= 1
        else:
            # If the stack is empty, we print an appropriate message
            print("Stack is empty")
        return pop_node

    def is_empty(self):
        """
        Check if stack is empty or not
        :return:
        """
        if self.length == 0:
            return True
        return False

    def print_stack(self):
        """
        Print method which prints the elements of the stack from top to bottom
        This will be an O(n) operation
        as we'll obviously have to traverse the entire linked list to print all elements
        :return:
        """
        if self.is_empty():
            print("Stack is empty")
        else:
            cur_node = self.top
            while cur_node:
                print(cur_node.value, end=" -->")
                cur_node = cur_node.next
            print()


my_stack = Stack()
my_stack.print_stack()
my_stack.push("google")
print(my_stack.peek())
my_stack.print_stack()

my_stack.push("udemy")
print(my_stack.peek())
my_stack.print_stack()

my_stack.push("youtube")
print(my_stack.peek())
my_stack.print_stack()

node = my_stack.pop()
print(node.value)
print(my_stack.peek())
my_stack.print_stack()

node = my_stack.pop()
print(node.value)
print(my_stack.peek())
my_stack.print_stack()

node = my_stack.pop()
my_stack.print_stack()
print(my_stack.peek())
my_stack.pop()
my_stack.print_stack()
