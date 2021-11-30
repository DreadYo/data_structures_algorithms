# Doubly linked lists are just normal, singly linked lists with one added feature,
# a link to the previous node as well in addition to a link to the next node.
# Although the worst case time complexities of all operations
# in a doubly linked list are same as that of a singly linked list,
# Some operations are technically faster.
# For example, lookup or searching, is O(n/2) as search can begin from both ends
# But O(n/2) = O(n), so it is still the same as that for a singly linked list.

# Look-up   -   O(n)
# Insert    -   O(n)
# Delete    -   O(n)
# Append    -   O(1)
# Prepend   -   O(1)


class Node:
    """
    Class Node which will act as a blueprint for each of our nodes
    """
    def __init__(self, value):
        """
        When instantiating a Node, we will pass the data we want the node to hold
        This self.next will act as a pointer to the next node in the list.
        This self.previous will act as a pointer to the previous node in the list.
        When creating a new node, it always points to null(or None).
        :param value: node's data
        """
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.__dict__)


class DoublyLinkedList:
    """
    Implementation of doubly linked list is almost exactly the same as that for singly linked list,
    With just the added feature of the pointer to the previous node.
    We'll have the same methods which do the exact same thing.
    The pars which will be different from the singly linked list are explained
    So lets implement it.

    Here, we will implement our own doubly linked list with some common methods such as
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
        Add element to the end of the Doubly Linked List
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
            new_node.previous = self._tail
            self._tail = new_node
            self._length += 1

    def prepend(self, value):               # Time Complexity - O(1)
        """
        Add element to the beginning of the Doubly Linked List
        :param value: value for adding
        :return:
        """
        new_node = Node(value)
        if self._head is None:
            self.append(value)
        else:
            new_node.next = self._head
            self._head.previous = new_node
            self._head = new_node
            self._length += 1

    def _traverse_to_index(self, index):    # Time Complexity - O(n)
        """
        Traverse to node with specific index in Linked List
        :param index: index to traverse
        :return:
        """
        if index < self._length / 2:
            current_node = self._head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self._tail
            for _ in range(self._length - index-1):
                current_node = current_node.previous
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
            after = self._traverse_to_index(index)
            pre = after.previous
            pre.next = new_node
            new_node.previous = pre
            new_node.next = after
            after.previous = new_node
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
            self._head.previous = None
            self._length -= 1
            return
        current_index = self._traverse_to_index(index)
        pre = current_index.previous
        after = current_index.next
        pre.next = after
        if after is not None:
            after.previous = pre
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
    my_doubly_linked_list = DoublyLinkedList()
    print(my_doubly_linked_list.print_list())
    # prepend
    my_doubly_linked_list.prepend(10)
    print(my_doubly_linked_list.print_list())
    # # append
    my_doubly_linked_list.append(5)
    print(my_doubly_linked_list.print_list())
    my_doubly_linked_list.append(16)
    print(my_doubly_linked_list.print_list())
    #
    my_doubly_linked_list.prepend(1)
    print(my_doubly_linked_list.print_list())
    print()
    # insert
    my_doubly_linked_list.insert(2, 99)
    print(my_doubly_linked_list.print_list())
    my_doubly_linked_list.insert(0, 0)
    print(my_doubly_linked_list.print_list())
    my_doubly_linked_list.insert(200, 200)
    print(my_doubly_linked_list.print_list())
    print()
    # # remove
    my_doubly_linked_list.remove(2)
    print(my_doubly_linked_list.print_list())
    my_doubly_linked_list.remove(5)
    print(my_doubly_linked_list.print_list())
    my_doubly_linked_list.remove(0)
    print(my_doubly_linked_list.print_list())

