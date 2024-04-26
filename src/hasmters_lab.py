
def recursive_dividing(left_position, right_position, available_food, counted_hamsters, hamsters_array):
    if right_position == left_position:
        middle_position = right_position
    else:
        middle_position = (left_position + right_position) // 2

    sorted_required_food_array = sorted([hamster[0] + hamster[1] * middle_position for hamster in hamsters_array])
    first_half_array_summary = sum(sorted_required_food_array[:middle_position + 1])

    if first_half_array_summary == available_food:
        return middle_position + 1

    elif first_half_array_summary > available_food:
        counted_hamsters[middle_position] = first_half_array_summary
        return recursive_dividing(right_position, middle_position - 1, available_food, counted_hamsters, hamsters_array)

    else:
        counted_hamsters[middle_position] = first_half_array_summary
        if counted_hamsters[middle_position + 1] > available_food:
            return middle_position + 1
        else:
            return recursive_dividing(middle_position + 1, right_position, available_food, counted_hamsters, hamsters_array)

def max_number_of_hamsters(available_food, number_of_hamsters, hamsters_array):
    left_position = 0
    right_position = number_of_hamsters - 1
    counted_hamsters = [0] * number_of_hamsters
    return recursive_dividing(left_position, right_position, available_food, counted_hamsters, hamsters_array)





