
def count_paths(width, height, corridor):
    counterrr = 0
    coordinate_map = create_symbol_coordinates_map(corridor)
    matrix = [[1] * width for _ in range(height)]
    for j in range(width - 1):
        for i in range(height):
            # print(corridor[i][j])
            matrix[i][j] = matrix[i][j-1]
            # print(matrix[i][j-1])
            counterrr += 1
            matrix[i][j] += count_symbols_with_lower_i_coordinate(coordinate_map, corridor[i][j], i, j, matrix)
    matrix[0][width - 1] = matrix[0][width - 2]
    matrix[0][width - 1] += count_symbols_with_lower_i_coordinate(coordinate_map, corridor[0][width-1], 0, width-1, matrix)

    matrix[height - 1][width - 1] = matrix[height - 1][width - 2]
    matrix[height - 1][width - 1] += count_symbols_with_lower_i_coordinate(coordinate_map, corridor[height - 1][width - 1], height - 1, width - 1, matrix)
    # print(matrix)
    # print(counterrr + 2)
    return matrix[0][width-1] + matrix[height-1][width-1]


def count_symbols_with_lower_i_coordinate(symbol_coordinates_map, symbol, i_coordinate,j_coordinate, matrix):
    count = 0

    if symbol in symbol_coordinates_map:
        # print(symbol + "    {" + str(i_coordinate) + "," + str(j_coordinate) + "}")
        for coord in symbol_coordinates_map[symbol]:
            if coord[1] < j_coordinate:
                if coord[1] != j_coordinate - 1 or coord[0] != i_coordinate:
                    # print(count)
                    count += matrix[coord[0]][coord[1]]
                    # print(count)
            # print(str(count) + " (" + str(coord[0]) + "," + str(coord[1]) + ")")

    # print(str(i_coordinate) + " " + str(j_coordinate) + " " + symbol + " " + str(matrix[i_coordinate][j_coordinate]))
    return count


def create_symbol_coordinates_map(corridor):
    symbol_coordinates_map = {}

    for i in range(len(corridor)):
        for j in range(len(corridor[i])):
            symbol = corridor[i][j]
            if symbol not in symbol_coordinates_map:
                symbol_coordinates_map[symbol] = []
            symbol_coordinates_map[symbol].append((i, j))

    return symbol_coordinates_map


def read_corridor_from_file(file_path):
    with open(file_path, 'r') as file:
        W, H = map(int, file.readline().split())
        corridor = [list(file.readline().strip()) for _ in range(H)]
    return W, H, corridor


def write_result_to_file(file_path, result):
    with open(file_path, 'w') as file:
        file.write(str(result))


# if __name__ == "__main__":
#     file_path = "ijones .in"
#     W, H, corridor = read_corridor_from_file(file_path)
#     result = count_paths(W, H, corridor)
#     print(result)
#     write_result_to_file("ijones.out", result)
