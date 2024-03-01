
def move_diagonally_up(row_idx, col_idx, rows_array_length, columns_array_length, arr, result_arr):
    while 0 < row_idx <= rows_array_length - 1 and 0 <= col_idx <= columns_array_length - 2:
        row_idx -= 1
        col_idx += 1
        curr_val = arr[row_idx][col_idx]
        result_arr.append(curr_val)
    return row_idx, col_idx


def move_diagonally_down(row_idx, col_idx, rows_array_length, columns_array_length, arr, result_arr):
    while 0 <= row_idx <= rows_array_length - 2 and 0 < col_idx <= columns_array_length - 1:
        row_idx += 1
        col_idx -= 1
        curr_val = arr[row_idx][col_idx]
        result_arr.append(curr_val)
    return row_idx, col_idx

def move_right(row_idx, col_idx, rows_array_length, columns_array_length, arr, result_arr):
    if col_idx != columns_array_length - 1:
        col_idx += 1
        curr_val = arr[row_idx][col_idx]
        result_arr.append(curr_val)
    return row_idx, col_idx

def move_down(row_idx, col_idx, rows_array_length, columns_array_length, arr, result_arr):
    if row_idx != rows_array_length - 1:
        row_idx += 1
        curr_val = arr[row_idx][col_idx]
        result_arr.append(curr_val)
    return row_idx, col_idx

def arr_zigzag_traverse(arr, rows_array_length, columns_array_length):
    result_arr = []

    row_idx = 0
    col_idx = 0
    curr_val = arr[row_idx][col_idx]
    result_arr.append(curr_val)

    if columns_array_length == 1:
        return arr

    while 0 <= row_idx <= rows_array_length - 1 and 0 <= col_idx <= columns_array_length - 1:

        if row_idx == rows_array_length - 1 and col_idx == columns_array_length - 2:
            move_right(row_idx, col_idx, rows_array_length, columns_array_length, arr, result_arr)
            return result_arr

        elif row_idx == 0 and col_idx >= 0 and col_idx != columns_array_length - 1:
            row_idx, col_idx = move_right(row_idx, col_idx, rows_array_length, columns_array_length, arr, result_arr)
            row_idx, col_idx = move_diagonally_down(row_idx, col_idx, rows_array_length, columns_array_length, arr, result_arr)

        elif row_idx == rows_array_length - 1 and col_idx >= 0 and col_idx != columns_array_length - 1:
            row_idx, col_idx = move_right(row_idx, col_idx, rows_array_length, columns_array_length, arr, result_arr)
            row_idx, col_idx = move_diagonally_up(row_idx, col_idx, rows_array_length, columns_array_length, arr, result_arr)

        elif row_idx != rows_array_length - 1 and col_idx == 0:
            row_idx, col_idx = move_down(row_idx, col_idx, rows_array_length, columns_array_length, arr, result_arr)
            row_idx, col_idx = move_diagonally_up(row_idx, col_idx, rows_array_length, columns_array_length, arr, result_arr)

        elif col_idx == columns_array_length - 1:
            row_idx, col_idx = move_down(row_idx, col_idx, rows_array_length, columns_array_length, arr, result_arr)
            row_idx, col_idx = move_diagonally_down(row_idx, col_idx, rows_array_length, columns_array_length, arr, result_arr)

test_array = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

print(arr_zigzag_traverse(test_array, 3, 3))

