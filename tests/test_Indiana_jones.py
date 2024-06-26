import unittest
from src.indiana_jones import *


class TestIJones(unittest.TestCase):
    def test_first_input(self):
        indiana_jones('../src/resources/indiana_input1.txt', '../src/resources/output_IJ1.txt')
        file = open('../output_IJ1.txt', 'r')
        result = file.readline()
        file.close()
        self.assertEqual(result, "5")

    def test_second_input(self):
        indiana_jones('../src/resources/input_file_for_IG2.txt', '../src/resources/output_IJ2.txt')
        file = open('../output_IJ2.txt', 'r')
        result = file.readline()
        file.close()
        self.assertEqual(result, "2")

    def test_third_input(self):
        indiana_jones('../src/resources/input_file_for_IG3.txt', 'output_IJ3.txt')
        file = open('../src/resources/output_IJ3.txt', 'r')
        result = file.readline()
        file.close()
        self.assertEqual(result, "201684")


if __name__ == '__main__':
    unittest.main()