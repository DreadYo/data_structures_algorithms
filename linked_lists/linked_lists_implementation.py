# Linked lists are, as the name suggests, a list which is linked.
# It consists of nodes which contain data and a pointer to the next node in the list.
# The list is connected with the help of these pointers.
# These nodes are scattered in memory, quite like the buckets in a hash table.
# The node where the list starts is called the head of the list
# and the node where it ends, or last node, is called the tail of the list.
# The average time complexity of some operations involving linked lists are as follows:

# Look-up   -   O(n)
# Insert    -   O(n)
# Delete    -   O(n)
# Append    -   O(1)
# Prepend   -   O(1)

# Python doesn't have a built-in implementation of linked lists, we have to build it on our own
# So, here we go.


class Node:
    """
    Class Node which will act as a blueprint for each of our nodes
    """
    def __init__(self, value):
        """
        When instantiating a Node, we will pass the data we want the node to hold
        This self.next will act as a pointer to the next node in the list.
        When creating a new node, it always points to null(or None).
        :param value: node's data
        """
        self.value = value
        self.next = None


class LinkedList:
    """
    Implement our Linked List class in Python.
    LinkedList have a head pointer to point to the beginning of the list and
    a tail pointer to point to the end of the list.
    An optional value of length can also be stored to keep track of the length of the linked list.

    Here, we will implement our own linked list with some common methods such as
    append, prepend, insert, remove
    """
    def __init__(self):
        """
        Linked list's constructor
        When the list is created , it is empty and there is no node to point to.
        So head will point to None at the time of creation of linked list
        And since the list is empty at the time of creation,
        we will point the tail to whatever the head is pointing to, i.e., None
        :param value:
        """
        self._head = None
        self._tail = self._head
        self._length = 0

    def append(self, value):                # Time Complexity - O(1)
        """
        Add element to the end of the Linked List
        :param value: value for adding
        :return:
        """
        # check params
        new_node = Node(value)
        if self._head is None:
            self._head = new_node
            self._tail = self._head
            self._length = +1
        else:
            self._tail.next = new_node
            self._tail = new_node
            self._length += 1

    def prepend(self, value):               # Time Complexity - O(1)
        """
        Add element to the beginning of the Linked List
        :param value: value for adding
        :return:
        """
        new_node = Node(value)
        if self._head is None:
            self.append(value)
        else:
            new_node.next = self._head
            self._head = new_node
            self._length += 1

    def _traverse_to_index(self, index):    # Time Complexity - O(n)
        """
        Traverse to node with specific index in Linked List
        :param index: index to traverse
        :return:
        """
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def insert(self, index, value):         # Time Complexity - O(n). Since this requires traversal of the list
        """
        Insert data at a specified position
        :param index:
        :param value:
        :return:
        """
        # check params
        if index < 0:
            print("Index can't be negative")
            return
        # if the position more than list length, then add to the end of list
        if index >= self._length:
            return self.append(value)
        # If the position is equal to 0, we follow the prepend procedure, where we append the node at the head
        elif index == 0:
            return self.prepend(value)
        else:
            new_node = Node(value)
            pre = self._traverse_to_index(index-1)
            after = pre.next
            new_node.next = after
            pre.next = new_node
            self._length += 1

    def remove(self, index):                # Time Complexity - O(n). Since this requires traversal of the list
        """
        Deleting a node based on its position.
        :param index:
        :return:
        """
        # check params
        if index >= self._length:
            print("Entered wrong index")
            return
        if self._head is None:
            print("Linked List is empty. Nothing to delete.")
            return
        if index == 0:
            self._head = self._head.next
            self._length -= 1
            return
        pre = self._traverse_to_index(index-1)
        current_index = pre.next
        pre.next = current_index.next
        self._length -= 1

    def print_list(self):
        """
        This will print the Linked List class in tuple format (array, length)
        :return: (array, length)
        """
        if self._head is None:
            return "empty"
        array = []
        current_node = self._head
        while current_node:
            array.append(current_node.value)
            current_node = current_node.next
        return array, self._length


if __name__ == '__main__':
    # create
    my_linked_list = LinkedList()
    print(my_linked_list.print_list())
    # prepend
    my_linked_list.prepend(10)
    print(my_linked_list.print_list())
    # append
    my_linked_list.append(5)
    print(my_linked_list.print_list())
    my_linked_list.append(16)
    print(my_linked_list.print_list())

    my_linked_list.prepend(1)
    print(my_linked_list.print_list())
    # insert
    my_linked_list.insert(2, 99)
    print(my_linked_list.print_list())
    my_linked_list.insert(0, 0)
    print(my_linked_list.print_list())
    my_linked_list.insert(200, 200)
    # remove
    print(my_linked_list.print_list())
    my_linked_list.remove(2)
    print(my_linked_list.print_list())
    my_linked_list.remove(5)
    print(my_linked_list.print_list())
    my_linked_list.remove(0)
    print(my_linked_list.print_list())

