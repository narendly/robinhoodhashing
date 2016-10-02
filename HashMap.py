###################################################################
# KPCB Engineering Fellows Program - Challenge Problem Submission #
# Applicant: Hunter Lee                                           #
# Email: hl130@duke.edu                                           #
###################################################################
import sys


class HashMap(object):

    def __init__(self, size: int):
        """Default constructor

        Instantiates an instance of HashMap for the given number of objects.
        Naive implementation of Hash Map using linear probing (open addressing).

        Args:
            size: size of the fixed-size hash map data structure

        """
        self.size = size
        self.key_list = [None] * self.size
        self.value_list = [None] * self.size
        self.num_items = 0
        # Probe lengths
        self.lengths = [None] * self.size

    def set(self, key: str, value):
        """Stores the given key/value pair in the hash map.

        Args:
            key: key string
            value: data object

        Returns:
            Boolean indicating success/failure of the operation

        """
        key, hash_index = self._process_key(key)

        for probe_length in range(self.size):
            # Key does not exist
            if self.key_list[hash_index] is None:
                self.key_list[hash_index], self.value_list[hash_index], self.num_items = key, value, self.num_items + 1
                # Record probe length
                self.lengths[hash_index] = probe_length
                return True
            # Key already exists - update
            elif self.key_list[hash_index] == key:
                self.value_list[hash_index] = value
                return True
            # Hash index is occupied - linear probing
            else:
                # Increment the index and try again
                hash_index = self._increment_hash(hash_index)
        return False

    def get(self, key: str):
        """Return the value associated with the given key.

        Args:
            key: key string

        Returns:
            the value associated with the key or None if the key has no value

        """
        key, hash_index = self._process_key(key)

        for probe_length in range(self.size):
            # Key matches, return value
            if self.key_list[hash_index] == key:
                return self.value_list[hash_index]
            # That index is null or keys don't match - linear probing
            # Can't terminate when it's null - items might have been deleted
            else:
                hash_index = self._increment_hash(hash_index)
        return None

    def delete(self, key):
        """Delete the key/value pair.

        Args:
            key: key string

        Returns:
            the value on success or None if the key has no value

        """
        # Check if HashMap is empty
        if self.load() == 0:
            return None

        key, hash_index = self._process_key(key)

        for probe_length in range(self.size):
            # Key matches, set it to None and return value
            if self.key_list[hash_index] == key:
                value = self.value_list[hash_index]
                self.key_list[hash_index], self.value_list[hash_index], self.num_items = None, None, self.num_items - 1
                return value
            # That index is null or keys don't match - linear probing
            else:
                hash_index = self._increment_hash(hash_index)
        return None

    def load(self):
        """Load

        Return a float value representing the load factor of the data structure.

        Returns:
            float: load factor
        """
        return self.num_items / self.size

    def clear(self):
        """Clears the content for testing purposes"""
        self.key_list.clear()
        self.value_list.clear()
        self.num_items = 0

    def _process_key(self, key: str):
        """Pre-processing step for key

        Use string interning to make lookup more efficient (done in Python's dict) and compute hash-based index.

        Args:
            key: string key

        Returns:
            key, hash_index tuple: string, int

        """
        key = sys.intern(key)
        return key, hash(key) % self.size

    def _increment_hash(self, index: int):
        """Internal hash incrementer

        Args:
            index: current hash index

        Return:
            incremented hash index

        """
        return (index + 1) % self.size

    @property
    def probe_lengths(self):
        """Getter for a list of probe lengths for statistics

        Returns:
            list of probe lengths for elements present

        """
        return [length for length in self.lengths if length is not None]

