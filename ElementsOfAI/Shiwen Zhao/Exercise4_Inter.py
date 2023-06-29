import random


def main():
    prob = 0.20
    x = random.random()
    if x > prob:
        output = "dog"
        print(output)
    else:
        output = "cat"
        print(output)


def test(x):
    prob = 0.20
    if x > prob:
        output = "dog"
        return output
    else:
        output = "cat"
        return output


main()
