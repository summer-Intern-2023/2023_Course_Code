import numpy as np
from io import StringIO


train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''


def main():
    # this just changes the output settings for easier reading
    np.set_printoptions(precision=1)

    # Please write your code inside this function

    # read in the training data and separate it to x_train and y_train
    train_data = StringIO(train_string)
    train_ = np.genfromtxt(train_data, skip_header=1)

    test_data = StringIO(test_string)
    test_ = np.genfromtxt(test_data, skip_header=1)

    train_x = np.asarray(
        train_[:, np.array([True, True, True, True, True, False])])
    train_y = np.asarray(
        train_[:, np.array([False, False, False, False, False, True])])

    x_test = np.asarray(
        test_[:, np.array([True, True, True, True, True, False])])
    y_test = np.asarray(
        test_[:, np.array([False, False, False, False, False, True])])

    # fit a linear regression model to the data and get the coefficients
    c = np.linalg.lstsq(train_x, train_y)[0]

    # print out the linear regression coefficients
    print(c.reshape(1, 5)[0])

    # this will print out the predicted prics for the two new cabins in the test data set
    sol = x_test @ c
    print(sol.reshape(1, 2)[0])


main()
