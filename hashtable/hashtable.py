class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    # Setters and getters for Node
    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_key(self):
        return self.key

    def __repr__(self):
        return f'LinkedList Node - key: {self.key}, value {self.value}'

class LinkedList:
    def __init__(self, key, value):
        self.head = HashTableEntry(key, value)
    
    def add_to_head(self, key, value):
        node = HashTableEntry(key, value)

        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def remove_from_head(self):
        if not self.head:
            return None
        
        temp = self.head
        self.head = temp.next

        return temp

    def get_value(self, key):
        current = self.head

        while (current):
            if current.get_key() == key:
                return current.get_value()
            
            current = current.next  

        return None

    def set_value(self, key, value):
        current = self.head

        while (current):
            if current.get_key() == key:
                current.set_value(value)
                break

            current = current.next  

            if not current:
                return 'key not found'       

    def check_for_key(self, key):
        current = self.head

        while(current):
            if current.get_key() == key:
                return True
            
            current = current.next
        
        return False

    def del_key(self, key):
        temp = self.head
        if not temp:
            return None
        # If key is in the head, del head
        elif temp.get_key() == key:
            self.head = self.head.next
            return temp.get_value()

        current = self.head.next

        while (current): 

            if current.get_key() == key:
                temp.next = current.next
                return current.get_value()

            temp = current
            current = current.next
        
        return 'key not found'


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        # Initialize emtpy array of at least min-capacity
        self.capacity = capacity
        self.arr = [None] * capacity

        # Counter for load factor
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # return legnth of array
        return len(self.arr)


    def load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        thresh = .7
        capacity = self.capacity

        # load factor is num of items divied by length of array
        load_factor = self.count / len(self.arr)

        # check if thresholds are exceeded and update capacity
        if load_factor > thresh:
            capacity *= capacity
            self.resize(capacity)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        hashed = 14695981039346656037 # fnv_offset_basis
        fnv_prime = 1099511628211
        encoded = key.encode('utf-8')

        for byte in encoded:
            hashed = hashed * fnv_prime
            hashed = hashed ^ byte

        return hashed



    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hashed = 5381
        encoded = key.encode('utf-8')

        for char in encoded:
            hashed = (( hashed << 5) + hashed) + char
    
        return hashed


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Get index using key
        idx = self.hash_index(key)

        # check for collisions
        if not self.arr[idx]:
            # if empty at location, create new LL object
            self.arr[idx] = LinkedList(key, value)

            self.count += 1

        # if key exist in LL, update value
        elif self.arr[idx].check_for_key(key):
            self.arr[idx].set_value(key,value)

        # Append value to list
        else:    
            self.arr[idx].add_to_head(key, value)
            self.count += 0

        # check load factor thresholds
        self.load_factor()

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Get index using key
        idx = self.hash_index(key)

        # check item in list 
        if not self.arr[idx]:
            return 'key not found'
        else:
        # delete item in this location
            self.arr[idx].del_key(key)

        # check load factor thresholds
        self.load_factor()
        

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # get index using key
        idx = self.hash_index(key)

        # return the value at that index
        return self.arr[idx].get_value(key)


    def resize(self, capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        #update capacity
        self.capacity = capacity

        #store current values
        temp_arr = self.arr

        #create arr of new length
        self.arr = [None] * self.capacity

        # itterate array of old values
        for item in temp_arr:
            # itterate LL
            if item:
                while True:
                    # pop head from LL
                    node = item.remove_from_head()
                    
                    # escape loop if node is empty
                    if not node:
                        break

                    # add items to new array
                    self.put(node.get_key(), node.get_value())
        
        del temp_arr


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
