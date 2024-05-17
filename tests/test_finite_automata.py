import unittest
from src.finite_automates import finite_automates_search

class TestFiniteAutomataSearch(unittest.TestCase):
    def test1_pattern_is_found(self):
        finite_automates = finite_automates_search("abc", "xabcy")
        self.assertEqual(finite_automates, [1])

    def test2_pattern_is_found(self):
        finite_automates = finite_automates_search("ababaca", "ababacababacabbb")
        self.assertEqual(finite_automates, [0, 6])

    def test_pattern_not_found(self):
        finite_automates = finite_automates_search("abc", "xaybzc")
        self.assertEqual(finite_automates, [])

    def test_empty_string(self):
        finite_automates = finite_automates_search("", "daadadsd")
        self.assertEqual(finite_automates, [])

    def test_empty_pattern(self):
        finite_automates = finite_automates_search("abc", "")
        self.assertEqual(finite_automates, [])

    def test_pattern_longer_than_string(self):
        finite_automates = finite_automates_search("abcdef", "abc")
        self.assertEqual(finite_automates, [])

    def test_same_pattern_and_string(self):
        finite_automates = finite_automates_search("abc", "abc")
        self.assertEqual(finite_automates, [0])


if __name__ == "__main__":
    unittest.main()