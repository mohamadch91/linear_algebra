import pandas as pd
import numpy as np

from matplotlib import pyplot as plt


# read date from file
def read(name):
    frame = pd.read_csv(name)
    return frame


# just read one column of file
def read_column(name):
    frame = read(name)
    open_list = frame.head(len(frame) - 10)['Open'].to_list()
    return open_list


# make coefficient matrix and answer matrix then get ans
def convert_to_mat_lin(name):
    # read from file
    list = read_column(name)
    # convert to array
    mat_ans = np.array(list)
    # reshape to matrix
    mat_ans = mat_ans.reshape(len(list), 1)
    coef_mat = np.zeros((len(list), 2))
    # make coeff matrix from rang values
    for i in range(1, len(list) + 1):
        coef_mat[i - 1] = [1, i]
    # transpose coeff matrix
    transpose_coef = coef_mat.transpose()
    # multiply transpose matrix with it
    coef_mat_dot = transpose_coef.dot(coef_mat)
    # multiply transpose matrix with ans matrix
    mat_ans_dot = transpose_coef.dot(mat_ans)
    # calculate answers of equation
    betas = np.linalg.solve(coef_mat_dot, mat_ans_dot)
    return betas


# make same things to non linear version of regration
def convert_to_mat_non_lin(name):
    list = read_column(name)
    mat_ans = np.array(list)
    mat_ans = mat_ans.reshape(len(list), 1)
    coef_mat = np.zeros((len(list), 3))
    # make coeff matrix of non linear regration
    for i in range(1, len(list) + 1):
        coef_mat[i - 1] = [1, i, i * i]
    # transpose coeff matrix
    transpose_coef = coef_mat.transpose()
    # multiply transpose matrix with coef matrix
    coef_mat = transpose_coef.dot(coef_mat)
    # multiply transpose matrix with answers matrix
    mat_ans = transpose_coef.dot(mat_ans)
    # calculate the answer of non linear equation
    betas = np.linalg.solve(coef_mat, mat_ans)
    return betas


def ans_reg(name):
    frame = read(name)
    # got answers from function
    ans = convert_to_mat_lin(name)
    ans_non = convert_to_mat_non_lin(name)
    ans_list = []
    ans_list_none = []
    # read open list from file
    open_list = frame.tail(10)['Open'].to_list()
    # calculate values from regration
    for i in range(len(frame) - 10, len(frame)):
        ans_list.append(ans[0] + ans[1] * i)
    # calculate values of non linear regration
    for k in range(len(frame) - 10, len(frame)):
        ans_list_none.append(ans_non[0] + ans_non[1] * k + ans_non[2] * k * k)
    # calculate difference of actual value and calculated one
    for s in range(len(ans_list)):
        print("calculated :{}".format(ans_list[s]))
        print("actual value :{}".format(open_list[s]))
        print(("error : {}".format(ans_list[s] - open_list[s])))
    # do same for non linear one
    print("NON LINEAR RESULT                       \n\n\n\n")
    for w in range(len(ans_list_none)):
        print("calculated :{}".format(ans_list_none[w]))
        print("actual value :{}".format(open_list[w]))
        print(("error : {}".format(ans_list_none[w] - open_list[w])))
    # calculate ans
    table = []
    # plot the answer of calculated value on table
    for p in range(1, len(frame) + 1):
        table.append(ans_non[0] + ans_non[1] * p + ans_non[2] * p * p)
    plt.plot(table, color='blue', label="guess values")
    # plot real values on table
    plt.scatter(range(len(frame.head(len(frame) - 10)['Open'].to_list())),
                frame.head(len(frame) - 10)['Open'].to_list(), color='red', label="Real value")
    plt.legend(loc="best")
    plt.show()


if __name__ == '__main__':
    # input file location
    name = input("please input file location : ")
    # gave to function to plot and calculate answers
    ans_reg(name)
