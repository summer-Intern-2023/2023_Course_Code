import random

def main():

    a = random.randint(1, 10)
    if a <= 8 :
        favourite = 'dogs'
    elif a == 9:
        favourite = 'bats'
    else:
        favourite = 'cats'
    print("I love " + favourite) 


main()