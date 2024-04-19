import unittest
import os

class TestGovernSorting(unittest.TestCase):
    def test_sorting(self):
        with open("../src/resources/govern.out", "r") as f:
            result = f.readlines()

        expected = [
            "birthcertificate\n",
            "nationalpassport\n",
            "militarycertificate\n",
            "foreignpassport\n",
            "creditcard\n",
            "hotel\n",
            "bankstatement\n",
            "visa\n"
        ]

        self.assertEqual(result, expected)

    def test_empty_file(self):

        self.assertTrue(os.path.exists("../src/resources/govern.out"), "Output file does not exist")

        with open("../src/resources/govern.out", "r") as f:
            result = f.readlines()
        self.assertTrue(result, "Output file is empty")



if __name__ == "__main__":
    unittest.main()