import csv


class DisjointSet:
    def __init__(self, n):
        self.parent = []
        for i in range(n):
            self.parent.append(i)
        self.rank = []
        for _ in range(n):
            self.rank.append(0)

    def find(self, elem1):
        while elem1 != self.parent[elem1]:
            self.parent[elem1] = self.parent[self.parent[elem1]]
            elem1 = self.parent[elem1]
        return elem1

    def union(self, elem1, elem2):
        root_elem1 = self.find(elem1)
        root_elem2 = self.find(elem2)

        if root_elem1 == root_elem2:
            return False

        if self.rank[root_elem1] < self.rank[root_elem2]:
            self.parent[root_elem1] = root_elem2
        else:
            self.parent[root_elem2] = root_elem1
            if self.rank[root_elem1] == self.rank[root_elem2]:
                self.rank[root_elem1] += 1
        return True


def kruskals_algo(graph):
    disjoint_set = DisjointSet(len(graph))
    edges = []
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))
    edges.sort()

    mst_edges = []
    min_weight = 0

    for weight, node1, node2 in edges:
        if disjoint_set.find(node1) != disjoint_set.find(node2):
            disjoint_set.union(disjoint_set.find(node1), disjoint_set.find(node2))
            min_weight += weight
            mst_edges.append((node1, node2))

    return min_weight, mst_edges


def read_graph_from_csv(filename):
    graph = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            graph.append(list(map(int, row)))
    return graph


def main():
    filename = 'resources/island.csv'
    graph = read_graph_from_csv(filename)

    min_cable_length, _ = kruskals_algo(graph)

    filename = 'resources/output.island'
    with open(filename, 'w') as output_file:
        output_file.write(str(min_cable_length))


if __name__ == "__main__":
    main()
