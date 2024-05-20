from typing import List, Tuple


def is_destination(row_position: int, column_position: int, rows: int, cols: int) -> bool:
    """
        Перевіряє, чи поточне поле є кінцевою точкою маршруту.

        :param row_position: Поточний рядок у матриці.
        :param column_position: Поточний стовпець у матриці.
        :param rows: Кількість рядків у матриці.
        :param cols: Кількість стовпців у матриці.
        :return: Логічне значення, чи є поточна позиція кінцевою точкою.
    """
    return (column_position == cols - 1 and row_position == 0) or (
                column_position == cols - 1 and row_position == rows - 1)


def receive_available_ways_to_move_from_current_field(row_position: int,
                                                      column_position: int,
                                                      matrix: List[List[str]],
                                                      cols: int,
                                                      rows: int) -> List[Tuple[int, int]]:
    """
        Отримує доступні напрямки руху з поточного поля.

        :param row_position: Поточний рядок у матриці.
        :param column_position: Поточний стовпець у матриці.
        :param matrix: Матриця поля.
        :param cols: Кількість стовпців у матриці.
        :param rows: Кількість рядків у матриці.
        :return: Список кортежів з координатами доступних напрямків руху.
    """

    current_letter = matrix[row_position][column_position]
    same_next_letter_positions = []
    for row in range(rows):
        for column in range(column_position + 1, cols):
            if matrix[row][column] == current_letter:
                same_next_letter_positions.append((row, column))

    if column_position + 1 < cols:
        next_position = (row_position, column_position + 1)
        if next_position not in same_next_letter_positions:
            same_next_letter_positions.append(next_position)

    return same_next_letter_positions


def indiana_jones_traversal(jumping: List[List[str]], rows: int, cols: int) -> int:
    """
        Пошук кількості успішних шляхів у коридорі за допомогою динамічного програмування.

        :param jumping: Матриця коридору.
        :param rows: Кількість рядків у матриці.
        :param cols: Кількість стовпців у матриці.
        :return: Кількість успішних шляхів в коридорі.
    """

    dynamic_programming_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    dynamic_programming_matrix[0][0] = 1

    for col in range(cols):
        for row in range(rows):
            if dynamic_programming_matrix[row][col] > 0:
                next_positions = receive_available_ways_to_move_from_current_field(row, col, jumping, cols, rows)
                for next_row, next_col in next_positions:
                    dynamic_programming_matrix[next_row][next_col] += dynamic_programming_matrix[row][col]

    result = 0
    for row in range(rows):
        if is_destination(row, cols - 1, rows, cols):
            result += dynamic_programming_matrix[row][cols - 1]

    return result


def read_input_matrix(path: str) -> Tuple[int, int, List[List[str]]]:
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read().strip().split("\n")
        matrix_size = data[0].split(" ")
        col_size = int(matrix_size[0])
        row_size = int(matrix_size[1])
        matrix = [list(line) for line in data[1:]]
    return row_size, col_size, matrix


def read_output(path: str) -> int:
    with open(path, 'r', encoding='utf-8') as file:
        return int(file.read().strip())


if __name__ == '__main__':
    row_size, col_size, sneaky_way = read_input_matrix("sources/i_jones1.in")
    result = indiana_jones_traversal(sneaky_way, rows=row_size, cols=col_size)
    print(result)
