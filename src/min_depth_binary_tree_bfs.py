from collections import deque


def read_binary_tree_input(file_name):
    with open(file_name, 'r') as f:
        root = int(f.readline())
        edges = [tuple(map(int, line.strip().split(','))) for line in f]

        adjacency_list = {}
        for u, v in edges:
            if u in adjacency_list:
                adjacency_list[u].append(v)
            else:
                adjacency_list[u] = [v]

    return root, adjacency_list

def min_depth_binary_tree_bfs(root, adjacency_list):
    if root not in adjacency_list:
        return 0

    visited = set()
    queue = deque([(root, 1)])

    while queue:
        current_node, depth = queue.popleft()
        if current_node not in visited:
            visited.add(current_node)
            if current_node not in adjacency_list:
                return depth
            for neighbor in adjacency_list[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, depth + 1))


def write_output(file_name, min_depth):
    with open(file_name, 'w') as file:
        file.write(str(min_depth))


if __name__ == "__main__":
    root, adjacency_list = read_binary_tree_input("resources/input.txt")
    min_depth = min_depth_binary_tree_bfs(root, adjacency_list)
    write_output("resources/output.txt", min_depth)