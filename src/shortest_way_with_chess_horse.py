from collections import deque

with open("../src/sources/input.txt") as file:
    N = int(file.readline())
    start_position = tuple(map(int, file.readline().strip().split(", ")))
    end_position = tuple(map(int, file.readline().strip().split(", ")))

row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]

visited = [[False] * N for _ in range(N)]


def is_move_possible(row_coordinate, column_coordinate):
    return 0 <= row_coordinate < N and 0 <= column_coordinate < N

def minimal_number_of_moves(start_position, end_position):
    queue_for_routes = deque([(start_position[0], start_position[1], 0)])
    visited[start_position[0]][start_position[1]] = True
    while queue_for_routes:
        row_coordinate, column_coordinate, moves = queue_for_routes.popleft()
        if (row_coordinate, column_coordinate) == end_position:
            return moves

        for move in range(8):
            available_row_coords, available_column_coords = row_coordinate + row[move], column_coordinate + col[move]
            if is_move_possible(available_row_coords, available_column_coords):
                queue_for_routes.append((available_row_coords, available_column_coords, moves + 1))
                visited[available_row_coords][available_column_coords] = True

    return -1

with open('../src/sources/output.txt', 'w') as file:
    file.write(str(minimal_number_of_moves(start_position, end_position)))




