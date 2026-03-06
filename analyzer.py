from collections import Counter


def digit_frequency(numbers):

    digits = []

    for n in numbers:
        digits.extend(list(n))

    return Counter(digits)


def position_frequency(numbers):

    pos = [[],[],[],[]]

    for n in numbers:

        if len(n)==4:

            pos[0].append(n[0])
            pos[1].append(n[1])
            pos[2].append(n[2])
            pos[3].append(n[3])

    return [Counter(p) for p in pos]