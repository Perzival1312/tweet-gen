from linked_list import LinkedList

class HashIter(object):
    def __init__(self, item):
        self.item = item  
        self.n = 0  

    def __next__(self):
        try:
            bucket = self.item[self.n]
        except:
            raise StopIteration
        self.n += 1
        return bucket

class HashTable(object):
    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.tot_length = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def __iter__(self):
        return HashIter(self.buckets)

    def __getitem__(self, key):
        if self.contains(key):
            return self.buckets[self._bucket_index(key)].find(lambda item : item[0] == key)[1]
        else:
            raise KeyError

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
         Running time: O(n) Why and under what conditions?
                goes through entire ht"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for pairs in bucket.items():
                all_keys.append(pairs[0])
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
         Running time: O(n) Why and under what conditions?
                goes through entire ht"""
        # Collect all values in each bucket
        all_vals = []
        for bucket in self.buckets:
            for pairs in bucket.items():
                all_vals.append(pairs[1])
        return all_vals

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
         Running time: O(n) Why and under what conditions?
                goes through entire ht"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
            Running time: O(1) Why and under what conditions?
                just reading single value"""
        return self.tot_length

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
         Running time: O(n) or O(1) Why and under what conditions?
                1 if key is in b0 head n if last item in ll of last bucket """
        bucket = self.buckets[self._bucket_index(key)] # bucket for specific key
        val = bucket.find(lambda item : item[0] == key) #tuple with specific key
        if val == None: # if dne
            return False
        else:
            return True

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
         Running time: O(n) Why and under what conditions?
                same as contains"""
        bucket = self.buckets[self._bucket_index(key)]  # Find bucket where given key belongs
        val = bucket.find(lambda item : item[0] == key)  # Check if key-value entry exists in bucket
        if val is not None:  # If found, return value associated with given key
            return val[1]
        else:  # Otherwise, raise error to tell user get failed
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
         Running time: O(n) Why and under what conditions?
                same as contains"""
        bucket = self.buckets[self._bucket_index(key)] # bucket for specific key
        val = bucket.find(lambda item : item[0] == key) #tuple with specific key
        if val == None: # if dne
            bucket.append((key, value)) # make it exist
            self.tot_length += 1
        else:
            bucket.replace(val, (key, value)) #replace the value

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
         Running time: O(n) Why and under what conditions?
                same as contains"""
        bucket = self.buckets[self._bucket_index(key)]  # Find bucket where given key belongs
        key_val = bucket.find(lambda item : item[0] == key)  # Check if key-value entry exists in bucket
        if key_val == None:  # Raise error to tell user delete failed
            raise KeyError('Key not found: {}'.format(key))
        # If found, delete entry associated with given key and adjust len accord.
        bucket.delete(key_val)
        self.tot_length -= 1


def test_hash_table():
    ht = HashTable(3)
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))
    print(ht['X'])

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))
    for thing in ht:
        for things in ht:
            print(thing, " + ", things)


if __name__ == '__main__':
    test_hash_table()