import unittest
from main import count_occurrences, unique_items

class TestDictionariesAndSets(unittest.TestCase):
    
    def test_count_occurrences(self):
        self.assertEqual(count_occurrences(["a", "b", "a", "c", "b", "a"]), {"a": 3, "b": 2, "c": 1})
        self.assertEqual(count_occurrences([]), {})
    
    def test_unique_items(self):
        self.assertEqual(unique_items({1, 2, 3}, {3, 4, 5}), {1, 2, 4, 5})
        self.assertEqual(unique_items(set(), set()), set())

if __name__ == '__main__':
    unittest.main()