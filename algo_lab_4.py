def has_cycle(graph, current, visited):
    visited[current + 1] = True

    for iterator in graph[current]:
        if visited[iterator]:
            return True
        if has_cycle(graph, iterator-1, visited):
            return True
    return False


def main():
    with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
        n, m = map(int, input_file.readline().split())
        graph = [[] for _ in range(n)]

        for _ in range(n):
            vertices = list(map(int, input_file.readline().split()))
            vertex_number = vertices[0]
            neighbors = [neighbor for neighbor in vertices[1:] if neighbor > vertex_number]
            graph[vertex_number - 1].extend(neighbors)
        visited = [None] + [False] * n
        cycle_exists = False
        for i in range(n):
            if not visited[i]:
                if has_cycle(graph, i, visited):
                    cycle_exists = True
                    break

        print(cycle_exists)
        output_file.write(str(cycle_exists))


if __name__ == "__main__":
    main()
