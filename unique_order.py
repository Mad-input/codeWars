def unique_in_order(sequence):
    unique_list = []

    for item in sequence:
        # Check if the current item is different from the previous one
        if not unique_list or item != unique_list[-1]:
            unique_list.append(item)

    return unique_list