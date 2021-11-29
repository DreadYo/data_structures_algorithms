class HashTable:
    """
    Hash tables are pre-defined in Python in the form of dictionaries.
    Implement our own Hash Table.
    Here, we will implement our own hash table with some common methods such as
    set, get, remove, keys, values
    """
    def __init__(self, size):
        # We initialize the size of our hash table(no. of buckets) with the size given to the class object
        self._size = size
        # We initialize an array of size 'size' with None
        self._data = [None] * self._size

    def __str__(self):
        """
        As in the array implementation, this method is used
        to print the attributes of the class object in a dictionary format
        :return:
        """
        return str(self.__dict__)

    def _hash(self, key):                       # Time Complexity - O(1)
        """
        #Our custom hash function
        :param key: hash table key
        :return: number between 0..size
        """
        hash = 0
        for i in range(len(key)):
            # ord(key[i]) gives the unicode code point of the character key[i]
            hash = (hash + ord(key[i]) * i) % self._size
        # The hash value obtained after applying the hash function to the key is returned
        return hash

    def set(self, key, value):                  # Time Complexity - O(1). When collision and bad hash function - O(n)
        """
        Function to insert a new key, value pair
        :param key:
        :param value:
        :return:
        """
        # Hash value of the key is calculated by passing the key to the _hash function
        index = self._hash(key)
        # If the 'hash' position of the data array is empty, we create a new empty array
        if not self._data[index]:
            self._data[index] = []
        # If the 'hash' position is not empty, implying a collision,
        # we simply append the list of key,value pair to the lists already present
        # When key is already exists in Hash Table, then rewrite value
        for i in range(len(self._data[index])):
            if self._data[index][i][0] == key:
                self._data[index][i][1] = value
                return None
        self._data[index].append([key, value])

    def get(self, key):                         # Time Complexity - O(1). When collision and bad hash function - O(n)
        """
        Function to return the value of the key entered by the user
        :param key:
        :return:
        """
        # Hash value of the key is calculated by passing the key to the _hash function
        index = self._hash(key)
        current_bucket = self._data[index]
        # Multiple items may exist in the position of the hash value returned by the hash function,
        # so we have to check all of them
        if current_bucket:
            # We loop over the entire list of lists that may be present in the 'hash' position of the data array
            for i in range(len(current_bucket)):
                # For every list in the list of lists(extracted by 'i'),
                # we match the first element of the list with the given key
                if current_bucket[i][0] == key:
                    # If we get a match, we return the second element of that list, which is the value
                    return current_bucket[i][1]
        # If we don't find the key, we return None
        return None

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :param key: to delete
        :return:
        """
        # Hash value of the key is calculated by passing the key to the _hash function
        index = self._hash(key)
        for i in range(len(self._data[index])):
            if self._data[index][i][0] == key:
                self._data[index].pop(i)
                return None
        return None

    def keys(self):
        """
        Function to return all keys
        :return:
        """
        # Array to hold keys
        keys_arr = []
        # We loop over the entire table
        for i in range(self._size):
            # If we find a non-empty bucket, we go in and loop over all the key,value pairs that might be in it
            if self._data[i]:
                if len(self._data[i]) > 1:
                    # Looping over all the lists(key,value pairs) in the current bucket
                    for j in range(len(self._data[i])):
                        # Adding the key of each list to the keys_array
                        keys_arr.append(self._data[i][j][0])
                else:
                    keys_arr.append(self._data[i][0][0])
        return keys_arr

    def values(self):
        """
        Function to return all values
        :return:
        """
        # Array to hold values
        val_arr = []
        # We loop over the entire table
        for i in range(self._size):
            # If we find a non-empty bucket, we go in and loop over all the key,value pairs that might be in it
            if self._data[i]:
                if len(self._data[i]) > 1:
                    # Looping over all the lists(key,value pairs) in the current bucket
                    for j in range(len(self._data[i])):
                        # Adding the value of each list to the val_arr
                        val_arr.append(self._data[i][j][1])
                else:
                    val_arr.append(self._data[i][0][1])
        return val_arr


my_hash_table = HashTable(2)
print(my_hash_table)

print(my_hash_table.keys())

# set
my_hash_table.set('grapes', 10000)
print(my_hash_table)

my_hash_table.set('apples', 10001)
print(my_hash_table)

my_hash_table.set('apple', 10003)
my_hash_table.set('potato', 10003)
print(my_hash_table)

my_hash_table.set('banana', 10005)
my_hash_table.set('banana', 10006)
my_hash_table.set('banana', 10007)
print(my_hash_table)

# get
print(my_hash_table.get("grapes"))
print(my_hash_table.get("banana"))

# remove
my_hash_table.remove("grapes")
print(my_hash_table)
my_hash_table.remove("banana")
print(my_hash_table)

# keys
print(my_hash_table.keys())
# values
print(my_hash_table.values())
