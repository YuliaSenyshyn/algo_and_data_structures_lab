class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class HeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def min_heapify_after_insert(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i].priority > self.heap[parent].priority:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def insert_elements(self, value, priority):
        new_node = Node(value, priority)
        self.heap.append(new_node)
        self.min_heapify_after_insert(len(self.heap) - 1)

    def min_heapify_after_delete(self, i):
        while i < len(self.heap):
            left_child = 2 * i + 1
            right_child = 2 * i + 2

            smallest = i
            if left_child < len(self.heap) and self.heap[left_child].priority < self.heap[smallest].priority:
                smallest = left_child
            if right_child < len(self.heap) and self.heap[right_child].priority < self.heap[smallest].priority:
                smallest = right_child

            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break

    def delete_elements(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.min_heapify_after_delete(0)
        return root

    def build_heap(self, heap):
        self.heap = heap
        i = len(heap) // 2 - 1
        while i >= 0:
            self.min_heapify_after_delete(i)
            i = i - 1
