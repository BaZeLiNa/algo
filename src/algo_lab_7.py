def count_paths(width, height, corridor):
    counter = 0
    internalMap = createMap(corridor)
    matrix = [[1] * width for _ in range(height)]
    for j in range(width - 1):
        myMap = internalMap.copy()

        for i in range(height):
            matrix[i][j] = matrix[i][j - 1]
            if corridor[i][j] == corridor[i][j - 1] and j > 0:
                matrix[i][j] = 0
            matrix[i][j] += myMap[corridor[i][j]]
            internalMap[corridor[i][j]] += matrix[i][j]
            counter += 1

    matrix[0][width - 1] = matrix[0][width - 2]
    if corridor[0][width - 1] == corridor[0][width - 2]:
        matrix[0][width - 1] = 0
    matrix[0][width - 1] += internalMap[corridor[0][width - 1]]

    matrix[height - 1][width - 1] = matrix[height - 1][width - 2]
    if corridor[height - 1][width - 1] == corridor[height - 1][width - 2]:
        matrix[height - 1][width - 1] = 0
    matrix[height - 1][width - 1] += internalMap[corridor[height - 1][width - 1]]

    return matrix[0][width - 1] + matrix[height - 1][width - 1]


def createMap(corridor):
    symbol_coordinates_map = {}

    for i in range(len(corridor)):
        for j in range(len(corridor[i])):
            symbol = corridor[i][j]
            if symbol not in symbol_coordinates_map:
                symbol_coordinates_map[symbol] = 0

    return symbol_coordinates_map


def read_corridor_from_file(file_path):
    with open(file_path, 'r') as file:
        W, H = map(int, file.readline().split())
        corridor = [list(file.readline().strip()) for _ in range(H)]
    return W, H, corridor


def write_result_to_file(file_path, result):
    with open(file_path, 'w') as file:
        file.write(str(result))


if __name__ == "__main__":
    file_path = "ijones .in"
    W, H, corridor = read_corridor_from_file(file_path)
    result = count_paths(W, H, corridor)
    print(result)
    write_result_to_file("ijones.out", result)
