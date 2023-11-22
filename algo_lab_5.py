from collections import defaultdict, deque


def topological_sort(graph):
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in graph if in_degree[node] == 0])
    result = []

    while queue:
        current_node = queue.popleft()
        result.append(current_node)

        for neighbor in graph[current_node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result


def optimal_order(government_data):
    graph = defaultdict(list)

    for line in government_data:
        parts = line.split()
        dependency, document = parts[0], parts[1]
        graph[document].append(dependency)

    order = topological_sort(graph)
    return order


with open("govern.in", "r") as file:
    government_data = file.read().splitlines()

optimal_order_result = optimal_order(government_data)

with open("govern.out", "w") as output_file:
    for document in optimal_order_result:
        output_file.write(document + "\n")

print("Optimal Order:", optimal_order_result)
