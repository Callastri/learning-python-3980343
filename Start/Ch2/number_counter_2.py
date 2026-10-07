def count_numbers(which, numbers):
    if which == "even":
        rest = 0
    elif which == "odd":
        rest = 1
    else:
        return -1

    counter = 0
    for n in numbers:
        if n % 2 == rest:
            counter += 1
    return counter