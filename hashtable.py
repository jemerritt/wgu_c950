class ChainHash:
    # Initialize hash table to 10 buckets
    # O(N)
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Insert value into hash table
    # O(N)
    def insert(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv_pair in bucket_list:
            if kv_pair[0] == key:
                kv_pair[1] = value
                return True

        key_value = [key, value]
        bucket_list.append(key_value)
        return True

    # Find and return value for the given key in hash table
    # O(N)
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv_pair in bucket_list:
            if kv_pair[0] == key:
                return kv_pair[1]
        return None

    # Delete entry from hash table with the given key
    # O(N)
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv_pair in bucket_list:
            if kv_pair[0] == key:
                bucket_list.remove([kv_pair[0], kv_pair[1]])

    # Update delivery status field for the package with given key
    # O(N)
    def update_status(self, key, value, time):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv_pair in bucket_list:
            if kv_pair[0] == key:
                kv_pair[1][8] = value
                kv_pair[1][9] = time
                return True

        return True

    # Update address id field for the package with given key
    # O(N)
    def update_address_id(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv_pair in bucket_list:
            if kv_pair[0] == key:
                kv_pair[1][7] = value
                return True

        return True
