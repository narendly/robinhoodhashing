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
        Implements Robin Hood hashing.

        Args:
            size: size of the fixed-size hash map data structure

        """
        self.size = size
        # key_list is a list of (key, probe_length) tuples
        self.key_list = [None] * self.size
        self.value_list = [None] * self.size
        self.num_items = 0

    def set(self, key: str, value):
        """Stores the given key/value pair in the hash map.

        Args:
            key: key string
            value: data object

        Returns:
            Boolean indicating success/failure of the operation

        """
        key, hash_index = self._process_key(key)
        probe_length = 0
        elem_to_swap, elem_to_swap_found, new_probe_length = None, False, 0
        while probe_length < self.size:
            # Key does not exist
            if self.key_list[hash_index] is None:
                # Store probe length with the key
                self.key_list[hash_index] = key, probe_length
                self.value_list[hash_index] = value
                self.num_items += 1
                # Swap if elem_to_swap has been found
                if elem_to_swap_found:
                    self._swap_elements(elem_to_swap, hash_index, new_probe_length)
                return True
            # Key already exists - update
            elif self.key_list[hash_index][0] == key:
                self.value_list[hash_index] = value
                return True
            # Hash index is occupied - linear probing
            else:
                # If existing element's probe length is lower, remember for swapping
                if elem_to_swap_found is False and self.key_list[hash_index][1] < probe_length:
                    elem_to_swap, elem_to_swap_found, new_probe_length = hash_index, True, probe_length
                # Increment the index and try again
                hash_index = self._increment_hash(hash_index)
            probe_length += 1
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
            if self.key_list[hash_index] is not None and self.key_list[hash_index][0] == key:
                return self.value_list[hash_index]
            # That index is null or keys don't match - linear probing
            # Can't terminate when it's null - items might have been deleted
            else:
                hash_index = self._increment_hash(hash_index)
        return None

    def delete(self, key: str):
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
            if self.key_list[hash_index] is not None and self.key_list[hash_index][0] == key:
                value = self.value_list[hash_index]
                self.key_list[hash_index], self.value_list[hash_index] = None, None
                self.num_items -= 1
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
            key: str

        Returns:
            (key: str, hash_index: int) tuple

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

    def _swap_elements(self, existing_index: int, new_index: int, new_probe_length: int):
        """Internal swap function

        Swap elements in the HashMap for lower variance in probe lengths. Implement Robin Hood hashing.

        Args:
            existing_index: index: int of an existing element with lower probe length
            new_index: index of the new element that has been inserted
            new_probe_length: new value for probe length for newly inserted element

        """
        # Calculate the new probe length for existing element
        delta = new_index - existing_index
        if delta < 0:
            delta = self.size - existing_index + new_index
        # Update probe lengths
        self.key_list[existing_index] = self.key_list[existing_index][0], self.key_list[existing_index][1] + delta
        self.key_list[new_index] = self.key_list[new_index][0], new_probe_length
        # Swap
        self.key_list[existing_index], self.key_list[new_index] = \
            self.key_list[new_index], self.key_list[existing_index]
        self.value_list[existing_index], self.value_list[new_index] = \
            self.value_list[new_index], self.value_list[existing_index]

    @property
    def probe_lengths(self):
        """Getter for a list of probe lengths for statistics

        Returns:
            list of probe lengths for elements present

        """
        return [probe_length[1] for probe_length in self.key_list if probe_length is not None]
