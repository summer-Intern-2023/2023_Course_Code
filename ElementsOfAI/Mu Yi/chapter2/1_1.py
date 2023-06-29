import numpy as np


def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0, 1], p=[1-p1, p1], size=10000)
    return seq


def count(seq):
    # insert code to return the number of occurrences of 11111 in the sequence
    count = 0
    consecutive_count = 0
    for char in seq:
        if char == 1:
            consecutive_count += 1
            if consecutive_count >= 5:
                count += 1
        else:
            consecutive_count = 0

    return count


def main(p1):
    seq = generate(p1)
    return count(seq)


print(main(2/3))
