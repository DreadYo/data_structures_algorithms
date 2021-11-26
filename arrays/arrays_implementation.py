class MyArray:
    """
    Arrays are pre-defined in Python in the form of lists.
    Implement our own arrays.
    Here, we will implement our own array with some common methods such as
    access, push, pop, insert, delete
    """
    def __init__(self):
        self._length = 0    # Initialize the array's length to be zero
        self._data = {}     # Initialize the data - empty dictionary. Keys - index, values - data

    def __str__(self):
        """
        This will print the attributes of the array class(length and data) in string format
        when print(array_instance) is executed
        :return:
        """
        return str(self.__dict__)

    @property
    def length(self):
        return self._length

    def get(self, index):
        """
        Takes in the index of the element as a parameter and returns the corresponding element in O(1) time.
        :param index: index of the element
        :return: corresponding element
        """
        if index >= self._length:
            raise IndexError("list index out of range")
        return self._data[index]

    def push(self, value):
        """
        Adds the item provided to the end of the array
        :param value: element for adding
        :return:
        """
        self._data[self._length] = value
        self._length += 1

    def pop(self):
        """
        Deletes the last element from the array. O(1) time
        :return: the popped element
        """
        last_item = self._data[self._length - 1]
        del self._data[self._length - 1]
        self._length -= 1
        return last_item

    def insert(self, index, value):
        """
        Inserts element in position in array
        O(n) operation
        :param index: index of the element for inserting
        :param value: the value of the element for inserting
        :return:
        """
        self._length += 1
        self._shift_right_items(index)
        self._data[index] = value

    def _shift_right_items(self, index):
        """
        Shifts elements from the given index to the end by one place right
        :param index: given index
        :return:
        """
        for i in range(self._length - 1, index, -1):
            self._data[i] = self._data[i - 1]

    def delete(self, index):
        """
        Deletes element from array by index
        :param index: index of deleted element
        :return:
        """
        item = self._data[index]
        self._shift_left_items(index)
        del self._data[self._length - 1]
        self._length -= 1
        return item

    def _shift_left_items(self, index):
        """
        Shifts elements from the given index to the end by one place towards left
        :param index: given index
        :return:
        """
        for i in range(index, self._length - 1):
            self._data[i] = self._data[i+1]


array = MyArray()
print(array)
print(f"length = {array.length}")

print("Test push")
print("array.push(1)")
array.push(1)
print("array.push(2)")
array.push(2)
print("array.push(3)")
array.push(3)
print("array.push(4)")
array.push(4)
print(array)
print(f"length = {array.length}")

print("Test pop")
print("array.pop()")
array.pop()
print(array)
print(f"length = {array.length}")
print("array.pop()")
array.pop()
print(array)
print(f"length = {array.length}")

print("Test get")
print(f"array.get(0) = {array.get(0)}")
print(f"array.get(1) = {array.get(1)}")


print("Test insert")
print("array.insert(0, 0)")
array.insert(0, 0)
print(array)
print(f"length = {array.length}")
print("array.insert(2, 3)")
array.insert(2, 3)
print(array)
print(f"length = {array.length}")
print("array.insert(array.length, 7)")
array.insert(array.length, 7)
print(array)
print(f"length = {array.length}")

print("Test delete")
print("array.delete(0)")
array.delete(0)
print(array)
print(f"length = {array.length}")

print("array.delete(2)")
array.delete(2)
print(array)
print(f"length = {array.length}")

print("array.delete(array.length-1)")
array.delete(array.length-1)
print(array)
print(f"length = {array.length}")

