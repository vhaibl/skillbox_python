counter = 0
r_counter = 0


def counters():
    global counter, r_counter

    counter = 0 if counter >= 100 else counter + 1
    r_counter = 0 if r_counter >= 6 else r_counter + 1
    return counter, r_counter
