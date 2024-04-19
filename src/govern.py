def read_graph_from_file(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            dependency, *dependents = line.strip().split()
            graph[dependency] = dependents
    return graph


def topological_sort(graph):
    in_degree = {}
    for node in graph:
        in_degree[node] = 0
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if neighbor not in in_degree:
                in_degree[neighbor] = 0
            in_degree[neighbor] += 1

    stack = []
    for node in graph:
        if in_degree.get(node, 0) == 0:
            stack.append(node)
    order = []

    while stack:
        node = stack.pop()
        order.append(node)

        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                stack.append(neighbor)

    return order


def write_order_to_file(order, file_path):
    with open(file_path, 'w') as file:
        for doc in reversed(order):
            file.write(doc + '\n')


def main():
    file_in_path = "resources/govern.in"
    file_out_path = "resources/govern.out"

    graph = read_graph_from_file(file_in_path)

    optimal_order = topological_sort(graph)
    write_order_to_file(optimal_order, file_out_path)
    print("Optimal order has been written to", file_out_path)


if __name__ == "__main__":
    main()
