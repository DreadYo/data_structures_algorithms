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


class Stack:
    """
    Implementation a stack using arrays
    """
    def __init__(self):
        """
        The constructor consists of only an empty array as length comes built-in with arrays(lists)
        """
        self.array = []

    def peek(self):
        """
        In the peek method we access the last element of the array(top element of the stack)
        Time complexity will be O(1)
        :return: the top element
        """
        if len(self.array) > 0:
            return self.array[-1]
        else:
            return "Stack is empty"

    def push(self, value):
        """
        For push operation, we use the built-in append method of lists,
        which appends/pushes/inserts an element at the end of the list(top of the stack)
        Time complexity is O(1)
        :param value: value to put in the stack
        :return:
        """
        self.array.append(value)

    def pop(self):
        """
        For pop operation, we use the built-in pop method of lists,
        which removes the last element of the list(top element of the stack)
        Its time complexity is O(1) as well
        :return:
        """
        pop_el = None
        if len(self.array) > 0:
            pop_el = self.array.pop()
        else:
            # If the stack is empty, we print an appropriate message
            print("Stack is empty")
        return pop_el

    def is_empty(self):
        """
        Check if stack is empty or not
        :return:
        """
        if len(self.array) == 0:
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
            print(f"[{'<--'.join(self.array)}]")
            print()


my_stack = Stack()
my_stack.print_stack()
print(my_stack.peek())
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
print(node)
print(my_stack.peek())
my_stack.print_stack()

node = my_stack.pop()
print(node)
print(my_stack.peek())
my_stack.print_stack()

node = my_stack.pop()
my_stack.print_stack()
print(my_stack.peek())
my_stack.pop()
my_stack.print_stack()
