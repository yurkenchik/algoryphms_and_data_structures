def next_state(pattern, state, symbol):
    if state < len(pattern) and symbol == pattern[state]:
        return state + 1

    pattern += symbol
    for i in range(state, 0, -1):
        prefix = pattern[0:i]
        suffix = pattern[-i:]
        if prefix == suffix:
            return i
    return 0

def transition_table(pattern, characters):
    table = [[0 for character in range(len(characters))] for _ in range(len(pattern) + 1)]
    for state in range(len(pattern) + 1):
        for symbol in characters:
            table[state][characters.index(symbol)] = next_state(pattern, state, symbol)
    return table

def finite_automates_search(pattern, haystack):
    if pattern and haystack and len(pattern) <= len(haystack):
        characters = list(sorted(set(haystack)))
        indices = []
        table = transition_table(pattern, characters)
        state = 0
        for i in range(len(haystack)):
            state = table[state][characters.index(haystack[i])]
            if state == len(pattern):
                indices.append(i - len(pattern) + 1)
        return indices
    else:
        return []