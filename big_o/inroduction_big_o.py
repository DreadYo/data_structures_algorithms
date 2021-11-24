from timeit import Timer

print("Big-O Introduction")

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']
large = ['nemo'] * 1000000

code1 = """
large = ['nemo'] * 1000000
def find_nemo(array):
    for el in array:
        if el == 'nemo':
            print("Found NEMO!")
find_nemo(large)
"""

code2 = """
large = ['nemo'] * 1000000
def find_nemo(array):
    for i in range(len(array)):
        if array[i] == 'nemo':
            print("Found NEMO!")
find_nemo(large)
"""

t1 = Timer(stmt=code1)
t2 = Timer(stmt=code2)
# time1 = t1.timeit(1)
# time2 = t2.timeit(1)

# print(f"Call to find Nemo took {time1} milliseconds")
# print(f"Call to find Nemo took {time2} milliseconds")

print("--------------")


def find_nemo(array):
    for el in array:
        if el == 'nemo':
            print("Found NEMO!")


# find_nemo(large)                # O(n) --> Linear Time

boxes = [i for i in range(5)]


def log_first_two_boxes(boxes):
    print(boxes[0])             # O(1) --> Constant Time
    print(boxes[1])             # O(1)


log_first_two_boxes(boxes)      # O(2) == O(1) == O(CONSTANT)


def fun_challenge(inp):
    a = 10                      # O(1)
    a = 50 + 3                  # O(1)

    for _ in range(len(inp)):
        # call another_func()   # O(n)
        stranger = True         # O(n)
        a += 1                  # O(n)
    return a                    # O(1)


# O(3 + 3n) = O(n)

def another_fun_challenge(inp):
    a = 5                       # O(1)
    b = 10                      # O(1)
    c = 50                      # O(1)

    for i in range(inp):
        x = i + 1               # O(n)
        y = i + 2               # O(n)
        z = i + 3               # O(n)

    for j in range(inp):
        p = j * 2               # O(n)
        q = j * 2               # O(n)

    who_i_am = "I don't know"   # O(1)

# O(4 + 5n) = O(n)


boxes = [1, 2, 3, 4, 5]


def all_pairs(array):           # O(n^2) --> Quadratic Time
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i], array[j])

all_pairs(boxes)
print("-----------")

