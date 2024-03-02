
def diag_up(row_idx, col_idx, rows_array_length, columns_array_lenght, arr, result_arr):
    while 0 < row_idx <= rows_array_length - 1 and 0 <= col_idx <= columns_array_lenght - 2:
        row_idx -= 1
        col_idx += 1
        curr_val = arr[row_idx][col_idx]
        result_arr.append(curr_val)
    return row_idx, col_idx

def diag_down(row_idx, col_idx, rows_array_lenght, columns_array_lenght, arr, result_arr):
    while 0 <= row_idx <= rows_array_lenght - 2 and 0 < col_idx <= columns_array_lenght - 1:
        row_idx += 1
        col_idx -= 1
        curr_val = arr[row_idx][col_idx]
        result_arr.append(curr_val)
    return row_idx, col_idx

def move_left(row_idx, col_idx, rows_array_lenght, columns_array_lenght, arr, result_arr):
    if 0 < col_idx <= columns_array_lenght - 1:
        col_idx -= 1
        curr_val = arr[row_idx][col_idx]
        result_arr.append(curr_val)
    return row_idx, col_idx

def move_up(row_idx, col_idx, rows_array_lenght, columns_array_lenght, arr, result_arr):
    if row_idx != 0:
        row_idx -= 1
        curr_val = arr[row_idx][col_idx]
        result_arr.append(curr_val)
    return row_idx, col_idx

def arr_zigzag_traversed(arr, rows_array_lenght, columns_array_lenght):
    result_arr = []
    row_idx = rows_array_lenght - 1
    col_idx = columns_array_lenght - 1
    curr_val = arr[row_idx][col_idx]
    result_arr.append(curr_val)

    if columns_array_lenght == 1:
        for row_idx in range(1, len(arr)):
            result_arr.append(arr[row_idx])
        return result_arr

    while 0 <= row_idx <= rows_array_lenght - 1 and 0 <= col_idx <= columns_array_lenght - 1:
        if row_idx == 0 and col_idx == 1:
            move_left(row_idx, col_idx, rows_array_lenght, columns_array_lenght, arr, result_arr)
            return result_arr

        elif row_idx == rows_array_lenght - 1 and 0 < col_idx <= columns_array_lenght - 1:
            row_idx, col_idx = move_left(row_idx, col_idx, rows_array_lenght, columns_array_lenght, arr, result_arr)
            row_idx, col_idx = diag_up(row_idx, col_idx, rows_array_lenght, columns_array_lenght, arr, result_arr)

        elif 0 < row_idx <= rows_array_lenght - 1 and col_idx == columns_array_lenght - 1:
            row_idx, col_idx = move_up(row_idx, col_idx, rows_array_lenght, columns_array_lenght, arr, result_arr)
            row_idx, col_idx = diag_down(row_idx, col_idx, rows_array_lenght, columns_array_lenght, arr, result_arr)

        elif 0 < row_idx <= rows_array_lenght - 1 and col_idx == 0:
            row_idx, col_idx = move_up(row_idx, col_idx, rows_array_lenght, columns_array_lenght, arr, result_arr)
            row_idx, col_idx = diag_up(row_idx, col_idx, rows_array_lenght, columns_array_lenght, arr, result_arr)

        elif row_idx == 0:
            row_idx, col_idx = move_left(row_idx, col_idx, rows_array_lenght, columns_array_lenght, arr, result_arr)
            row_idx, col_idx = diag_down(row_idx, col_idx, rows_array_lenght, columns_array_lenght, arr, result_arr)

test_array = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

print(arr_zigzag_traversed(test_array, 3, 3))

