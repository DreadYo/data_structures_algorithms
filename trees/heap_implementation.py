"""
A heap is a tree where every parent is greater than its children ( for max-heaps )
or they are smaller than their children ( for min-heaps)
A Max heap( and min heap) is typically represented as an array.
The root element will be at Arr[0].
Arr[(i-1)/2] Returns the parent node.
Arr[(2*i)+1] Returns the left child node.
Arr[(2*i)+2] Returns the right child node.
Operations on Max Heap (and min heap) include:
 - getMax(): It returns the root element of Max Heap. Time Complexity of this operation is O(1).
 - extractMax(): Removes the maximum element from MaxHeap. Time Complexity of this Operation is O(Log n)
as this operation needs to maintain the heap property (by calling heapify()) after removing root.
 - insert(): Inserting a new key takes O(Log n) time. We add a new key at the end of the tree.
If new key is smaller than its parent, then we don’t need to do anything.
Otherwise, we need to traverse up to fix the violated heap property.
Here we are going to implement a max-heap

Lookup      -   O(n)
Insert      -   O(logn)
Delete      -   O(logn)

Binary Heap is very efficient if you need to do some COMPARATIVE operations,
for example to get things (numbers) more than given number.

"""


class MaxHeap:
    def __init__(self, maxsize):
        """
        The constructor initializes the heap with a maxsize entered by the user,
        size set to 0, all the elements of heap set to 0
        :param maxsize:
        """
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * self.maxsize

    def parent(self, pos):
        """
        Method to return the position of parent for the node currently at pos
        :param pos:
        :return:
        """
        return (pos - 1)//2

    def left_child(self, pos):
        """
        Method to return the position of the left child for the node currently at pos
        :param pos:
        :return:
        """
        return 2 * pos + 1

    def right_child(self, pos):
        """
        Method to return the position of the right child for the node currently at pos
        :param pos:
        :return:
        """
        return 2 * pos + 2

    def is_leaf(self, pos):
        """
        Method that returns true if the passed node is a leaf node.
        All the nodes in the second half of the heap(when viewed as an array) are leaf nodes.
        So we just check if the position entered is >= half of the size of the heap and <= size of the heap
        :param pos:
        :return:
        """
        if self.size // 2 <= pos < self.size:
            return True
        return False

    def swap(self, first_pos, second_pos):
        """
        Method to swap two nodes of the heap
        :param first_pos:
        :param second_pos:
        :return:
        """
        self.heap[first_pos], self.heap[second_pos] = self.heap[second_pos], self.heap[first_pos]

    def insert(self, element):
        """
        Method to insert a node into the heap .
        First we will increase the size of the heap by 1.
        Then we will insert the element to end of the heap.
        Now this new element may violate the heap property.
        So we will keep checking its value with its parent's value.
        And keep swapping it with its parent as long as the parent is smaller than the element.
        :param element:
        :return:
        """
        if self.size >= self.maxsize:
            return
        self.heap[self.size] = element
        current = self.size
        while self.heap[current] > self.heap[self.parent(current)] and current != 0:
            self.swap(current, self.parent(current))
            current = self.parent(current)
        self.size += 1

    def print_heap(self):
        """
        Method to print the contents of the heap in a detailed format
        :return:
        """
        for i in range(self.size//2):
            print(f"parent: {self.heap[i]} left child: {self.heap[self.left_child(i)]} "
                  f"right child: {self.heap[self.right_child(i)]}")

    def max_heapify(self, pos):
        """
        Method to heapify the node at pos.
        This method will be called whenever the heap property is disturbed,
        to restore the heap property of the heap
        We will check if the concerned node is a leaf node or not first.
        If it is, then no need to do anything.
        If it is not and it is smaller than any of its children, then we will check which of its children is largest
        and swap the node with its largest child.
        After doing this, the heap property may be disturbed.
        So we will call max_heapify again.
        :param pos:
        :return:
        """
        # If the node is a non-leaf node and smaller than any of its child
        if not self.is_leaf(pos):
            if (self.heap[pos] < self.heap[self.left_child(pos)] or
                    self.heap[pos] < self.heap[self.right_child(pos)]):
                # Swap with the left child and heapify the left child
                if self.heap[self.left_child(pos)] > self.heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.max_heapify(self.left_child(pos))
                # Swap with the right child and heapify the right child
                else:
                    self.swap(pos, self.right_child(pos))
                    self.max_heapify(self.right_child(pos))

    def extract_max(self):
        """
        Method to remove and return the maximum element from the heap.
        The maximum element will be at the root.
        So we will copy the element at the end of the heap into the root node and delete the last node,
        which will leave the heap property disturbed
        So we will finally call heapify on the root node to restore the heap property
        :return:
        """
        popped = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.max_heapify(0)
        return popped


if __name__ == "__main__":
    my_heap = MaxHeap(15)
    print(my_heap.heap)
    my_heap.insert(5)
    my_heap.insert(3)
    my_heap.insert(17)
    my_heap.insert(10)
    my_heap.insert(84)
    my_heap.insert(19)
    my_heap.insert(6)
    my_heap.insert(22)
    my_heap.insert(9)

    my_heap.print_heap()
    print(my_heap.heap)

    print("The Max val is " + str(my_heap.extract_max()))
    # The Max val is 84

    my_heap.print_heap()

    print()
    my_heap.insert(100)

    my_heap.print_heap()
    print(my_heap.heap)
