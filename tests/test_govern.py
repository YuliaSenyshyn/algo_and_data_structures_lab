import unittest
from src.govern import *

class TestTopologicalSort(unittest.TestCase):
    def test_empty_graph(self):
        graph = {}
        expected_order = []
        self.assertEqual(topological_sort(graph), expected_order)

    def test_single_dependency(self):
        graph = {
            'visa': ['foreignpassport', 'hotel', 'bankstatement'],
            'bankstatement': ['nationalpassport'],
            'hotel': ['creditcard'],
            'creditcard': ['nationalpassport'],
            'nationalpassport': ['birthcertificate'],
            'foreignpassport': ['nationalpassport', 'militarycertificate'],
            'militarycertificate': ['nationalpassport']
        }
        expected_order = ['visa', 'bankstatement', 'hotel', 'creditcard', 'foreignpassport', 'militarycertificate', 'nationalpassport', 'birthcertificate']
        self.assertEqual(topological_sort(graph), expected_order)

    def test_multiple_dependencies(self):
        graph = {
            'visa': ['foreignpassport', 'hotel', 'bankstatement'],
            'bankstatement': ['nationalpassport'],
            'hotel': ['creditcard'],
            'creditcard': ['nationalpassport'],
            'nationalpassport': ['birthcertificate'],
            'foreignpassport': ['nationalpassport', 'militarycertificate'],
            'militarycertificate': ['nationalpassport']
        }
        expected_order = ['visa', 'bankstatement', 'hotel', 'creditcard', 'foreignpassport', 'militarycertificate', 'nationalpassport', 'birthcertificate']
        self.assertEqual(topological_sort(graph), expected_order)

if __name__ == '__main__':
    unittest.main()