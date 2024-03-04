
def find_max_number_of_hamsters(S, C, hamsters_array):

    def sort_hamster_by_greed():
        for outer in range(0, len(hamsters_array) - 1):
            for inner in range(0, len(hamsters_array) - 1):
                if hamsters_array[inner][1] > hamsters_array[inner + 1][1]:
                    hamsters_array[inner], hamsters_array[inner + 1] = hamsters_array[inner + 1], hamsters_array[inner]

        return hamsters_array

    sort_hamster_by_greed()
    hamsters_counter = 1

    for hamster in range(C):
        daily_portion = hamsters_array[hamster][0]
        greed = hamsters_array[hamster][1]

        number_of_neighbors = C - 1
        needed_food = daily_portion + greed * number_of_neighbors

        if needed_food <= S:
            hamsters_counter += 1
            S -= needed_food
        else:
            break

    return hamsters_counter





