import pandas as pd
import numpy as np
import math
from matplotlib import pyplot as plt

def read(name):
    frame=pd.read_csv(name)
    return frame
def read_column(name):
    frame=read(name)
    open_list=frame.head(len(frame)-10)['Open'].to_list()
    return open_list
def convert_to_mat_lin(name):
    list=read_column(name)
    mat_ans=np.array(list)
    mat_ans=mat_ans.reshape(len(list),1)
    coef_mat=[]
    for i in range(1,len(list)+1):
        coef_mat.append(1)
        coef_mat.append(i)
    coef_mat=np.array(coef_mat)
    coef_mat=coef_mat.reshape(len(list),2)
    transpose_coef=coef_mat.transpose()
    coef_mat=transpose_coef.dot(coef_mat)
    mat_ans=transpose_coef.dot(mat_ans)
    # augmented_mat=np.hstack(coef_mat,mat_ans)
    # augmented_mat=np.concatenate((coef_mat,mat_ans),axis=1)
    betas=np.linalg.solve(coef_mat,mat_ans)
    return betas
def convert_to_mat_non_lin(name):
    list = read_column(name)
    mat_ans = np.array(list)
    mat_ans = mat_ans.reshape(len(list), 1)
    coef_mat = []
    for i in range(1, len(list) + 1):
        coef_mat.append(1)
        coef_mat.append(i)
        coef_mat.append(i*i)
    coef_mat = np.array(coef_mat)
    coef_mat = coef_mat.reshape(len(list), 2)
    transpose_coef = coef_mat.transpose()
    coef_mat = transpose_coef.dot(coef_mat)
    mat_ans = transpose_coef.dot(mat_ans)
    # augmented_mat=np.hstack(coef_mat,mat_ans)
    # augmented_mat = np.concatenate((coef_mat, mat_ans), axis=1)
    betas = np.linalg.solve(coef_mat, mat_ans)
    return betas
def ans_reg(name):
    frame=read(name)
    ans=convert_to_mat_lin(name)
    ans_non=convert_to_mat_non_lin(name)
    ans_list=[]
    ans_list_none=[]
    open_list=frame.tail(10)['Open'].to_list()
    for i in range(len(frame)-10,len(frame)):
        ans_list.append(ans[1]+ans[2]*i)
    for k in range(len(frame)-10,len(frame)):
        ans_list_none.append(ans_non[0]+ans_non[1]*k+ans_non[2]*k*k)
    for s in range(len(ans_list)):
        print("calculated :{}".format(ans_list[s]))
        print("actual value :{}".format(open_list[s]))
        print(("error : {}".format(ans_list[s]-open_list[s])))
    for w in range(len(ans_list_none)):
        print("calculated :{}".format(ans_list_none[w]))
        print("actual value :{}".format(open_list[w]))
        print(("error : {}".format(ans_list_none[w] - open_list[w])))
    #calculate ans
    table=[]
    for p in range (1,len(frame)+1):
        table.append(ans_non[0]+ans_non[1]*p+ans_non[2]*p*p)
    plt.plot(table,color='blue')
    plt.scatter(range(len(open_list)),open_list,color='red')
    plt.legend("best")





