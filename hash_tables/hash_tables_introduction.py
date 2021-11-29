# Hash Tables are data structures which generally provide very fast(O(1)) lookups, insertions and deletions
# In Python, dictionaries are implemented as hash tables.

# The way hashing works is that there is a bucket containing slots to fill with elements.

# But in some cases, more than one keys can map to the same slot and
# that increases the time complexity by some margin,
# although not by a lot in most cases.
# This is known as a collision.
# Now, like for almost all problem there is some sort of a solution in the computer science world,
# collisions can also be resolved by numerous collison resolution techniques
# like open addressing and closed addressing

# lookup/access -   O(1)
# insert        -   O(1)
# delete        -   O(1)
# search        -   O(1)



user = {
    "age": 54,
    "name": "Kylie",
    "magic": True,
    "scream": lambda: print('ahhhhh!')
}

print(user["age"])                  # O(1)
user["spell"] = "abra kadabra"      # O(1)
print(user)

user["scream"]()                    # O(1)

# With collision:
# reading       -   O(n/k) = O(n)       where k - size of hash table
# writing       -   O(n/k) = O(n)       where k - size of hash table
