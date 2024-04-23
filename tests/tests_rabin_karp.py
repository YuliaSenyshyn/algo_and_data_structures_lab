import unittest
from src.rabin_karp import rabin_karp

class RabinKarpTest(unittest.TestCase):
    def test_empty_needle(self):
        self.assertEqual(rabin_karp("abracadabra", ""), [])

    def test_single_character_needle(self):
        self.assertEqual(rabin_karp("abracadabra", "a"), [0, 3, 5, 7, 10])

    def test_multiple_occurrences(self):
        self.assertEqual(rabin_karp("abracadabra", "abra"), [0, 7])

    def test_no_occurrences(self):
        self.assertEqual(rabin_karp("abracadabra", "xyz"), [])

    def test_longer_needle(self):
        self.assertEqual(rabin_karp("abracadabracadabra", "abracadabra"), [0, 7])


if __name__ == "__main__":
    unittest.main()