###################################################################
# KPCB Engineering Fellows Program - Challenge Problem Submission #
# Applicant: Hunter Lee                                           #
# Email: hl130@duke.edu                                           #
###################################################################
import unittest
import string
import random
import statistics
from HashMapRH import HashMap as robinhood
from HashMap import HashMap as naive


class TestHashMap(unittest.TestCase):
    def test_hashmap(self, hash_type="robinhood", hash_map_size=50):
        """Tests the hash map data structure

        Args:
            type: type of the hash map to use

        """
        # Initialize
        print("Initializing a hash map ...")
        hash_map = naive(hash_map_size) if hash_type == "naive" else robinhood(hash_map_size)

        # Load factor test
        print("Load factor test ...")
        self.assertEqual(0.0, hash_map.load())

        # Add key/value pairs
        values = []
        for _ in range(hash_map_size):
            value = self.value_generator()
            hash_map.set(str(_), value)
            values.append(value)

        # Load factor test
        self.assertEqual(1.0, hash_map.load())

        # Get test
        print("Get test ...")
        for _ in range(hash_map_size):
            self.assertEqual(values[_], hash_map.get(str(_)))

        # Delete test
        print("Delete test ...")
        del_index = random.randint(0, hash_map_size)
        self.assertEqual(values[del_index], hash_map.delete(str(del_index)))
        self.assertEqual(None, hash_map.delete(str(del_index)))

        # Load factor test
        self.assertEqual((hash_map_size - 1) / hash_map_size, hash_map.load())

        # Set test
        print("Set test ...")
        self.assertEqual(True, hash_map.set(str(del_index), values[del_index]))

        # Load factor test
        self.assertEqual(1.0, hash_map.load())

        # Get statistics (variance)
        print("Variance is {}".format(statistics.variance(hash_map.probe_lengths)))

        print("Testing finished successfully ...")

    def value_generator(self, size=10, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

if __name__ == '__main__':
    unittest.main()
