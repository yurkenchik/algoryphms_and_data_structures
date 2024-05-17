from typing import List

def is_destination(wanted_destination: bool, row_position: int, column_position: int, rows: int, cols: int) -> bool:
    """
        Перевіряє, чи поточне поле є точкою, до якої потрібно дістатися.

        :param wanted_destination: Очікувана кінцева точка (True/False).
        :param row_position: Поточний рядок у матриці.
        :param column_position: Поточний стовпець у матриці.
        :param rows: Кількість рядків у матриці.
        :param cols: Кількість стовпців у матриці.
        :return: Логічне значення, чи є поточна позиція кінцевою точкою.
    """

    if wanted_destination:
        return (column_position == cols - 1 and row_position == 0) or (column_position == cols - 1 and row_position == rows - 1)
    return column_position == cols - 1 and 0 < row_position < rows - 1

def receive_available_ways_to_move_from_current_field(row_position: int,
                                                      column_position: int,
                                                      matrix: List[List[str]],
                                                      cols: int,
                                                      rows: int) -> List:
    """
        Отримує доступні напрямки руху з поточного поля.

        :param row_position: Поточний рядок у матриці.
        :param column_position: Поточний стовпець у матриці.
        :param matrix: Матриця поля.
        :param cols: Кількість стовпців у матриці.
        :param rows: Кількість рядків у матриці.
        :return: Список кортежів з координатами доступних напрямків руху.
    """

    # проходимось по матриці, щоб знайти наступні однакові позиції літер
    current_letter = matrix[row_position][column_position]
    same_next_letter_positions = []
    for row in range(rows):
        for column in range(column_position + 1, cols):
            letter = matrix[row][column]
            if letter == current_letter:
                same_next_letter_positions.append((row, column))

    # в цьому циклі ми перевіряємо чи справа є наступна позиція
    if column_position + 1 < cols:
        next_position = (row_position, column_position + 1)
        if next_position not in same_next_letter_positions:
            same_next_letter_positions.append(next_position)
    return same_next_letter_positions

    return total_ways

def indiana_jones_traversal(jumping: List[List[str]],
                            rows: int,
                            cols: int,
                            row_position: int = 0,
                            column_position: int = 0,
                            memo: dict = None) -> int:
    """
        Пошук кількості успішних шляхів у коридорі за допомогою рекурсивного методу з мемоізацією.

        :param jumping: Матриця коридору.
        :param rows: Кількість рядків у матриці.
        :param cols: Кількість стовпців у матриці.
        :param row_position: Початковий рядок у матриці (за замовчуванням 0).
        :param column_position: Початковий стовпець у матриці (за замовчуванням 0).
        :param memo: Словник для збереження результатів обчислень (за замовчуванням None).
        :return: Кількість успішних шляхів в коридорі.
    """

    if memo is None:
        memo = {}

    # Перевірка чи ми вже обчислювали цю позицію
    if (row_position, column_position) in memo:
        return memo[(row_position, column_position)]

    # тут ми перевіряємо чи поточне поле є точкою, до якої нам треба дістатись чи ні
    if is_destination(True, row_position, column_position, rows, cols):
        memo[(row_position, column_position)] = 1
        return 1
    if is_destination(False, row_position, column_position, rows, cols):
        memo[(row_position, column_position)] = 0
        return 0

    # тут ми отримуємо наступні поля, до яких ми можемо дібратись
    next_available_fields = receive_available_ways_to_move_from_current_field(row_position,
                                                                              column_position,
                                                                              jumping,
                                                                              cols=cols,
                                                                              rows=rows)
    total_ways = 0

    # ітеруємо через усі доступні наступні поля і рекурсивно додаємо їх до загальної к-сті шляхів
    for field in next_available_fields:
        total_ways += indiana_jones_traversal(
            jumping,
            rows=rows,
            cols=cols,
            row_position=field[0],
            column_position=field[1],
            memo=memo
        )

    # тут ми зберігаємо результат в мемозуаційному словнику
    memo[(row_position, column_position)] = total_ways

    return total_ways



def read_input_matrix(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
        data = data.split("\n")

        matrix_length = data[0].split(" ")
        col_size = int(matrix_length[0])
        row_size = int(matrix_length[1])

        sneaky_way = [list(data[i]) for i in range(1, len(data))]
    return row_size, col_size, sneaky_way


def read_output(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
    return int(data)


if __name__ == '__main__':
    row_size, col_size, sneaky_way = read_input_matrix("sources/i_jones1.in")
    result = indiana_jones_traversal(sneaky_way, rows=row_size, cols=col_size)
    print(result)
