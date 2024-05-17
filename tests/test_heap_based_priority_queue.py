import unittest
from src.heap_based_priority_queue import HeapPriorityQueue, Node


class TestHeapPriorityQueue(unittest.TestCase):

    def test_is_empty(self):
        queue = HeapPriorityQueue()
        self.assertEqual(len(queue.heap), 0)

    def test_is_not_empty_after_insert(self):
        queue = HeapPriorityQueue()
        queue.insert_elements("test", 1)
        self.assertNotEqual(len(queue.heap), 0)

    def test_insert_and_delete_min_with_equal_priorities(self):
        queue = HeapPriorityQueue()
        queue.insert_elements('Task 4', 4)
        queue.insert_elements('Task 5', 4)
        queue.insert_elements('Task 6', 4)

        self.assertEqual(queue.delete_elements().value, 'Task 4')
        self.assertEqual(queue.delete_elements().value, 'Task 6')
        self.assertEqual(queue.delete_elements().value, 'Task 5')

    def test_build_heap(self):
        queue = HeapPriorityQueue()
        queue.build_heap([Node('Task 10', 2), Node('Task 11', 1), Node('Task 12', 3)])

        self.assertEqual(queue.delete_elements().value, 'Task 11')
        self.assertEqual(queue.delete_elements().value, 'Task 10')
        self.assertEqual(queue.delete_elements().value, 'Task 12')


if __name__ == "__main__":
    unittest.main()
