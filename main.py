import numpy as np
import math

def make_num_valid(matrix, row, column):
    num = matrix[row, column]
    if math.ceil(num) - num < 0.00000000001:
        matrix[row, column] = math.ceil(num)
    elif  num - math.floor(num)<0.00000000001  :
      matrix[row,column]=math.floor(num)
def make_num_valid_calc(num):

    if math.ceil(num) - num < 0.00000000001:
        num=math.ceil(num)
    elif num - math.floor(num) < 0.00000000001:
        num = math.floor(num)
    return num
# # np.format_float_positional(True)
np.set_printoptions(3,suppress=True)

# np.format_float_scientific(False)
print("enter row on column please\n>")
row = int(input())
columns = int(input())
zarayeb_matrix = []
for i in range(row):
    print("please enter row {} : \n>".format(i + 1))
    for j in range(columns):
        zarayeb_matrix.append(float(input()))

answer_matrix = []
print('enter constant values: \n >')
for i in range(row):
    answer_matrix.append(float(input()))
zarayeb_matrix = np.array(zarayeb_matrix).reshape(row, columns)
answer_matrix = np.array(answer_matrix).reshape(row, 1)
answer_matrix = np.array(answer_matrix[:, -1]).reshape(-1, 1)
augmented_matrix = np.hstack(((zarayeb_matrix, answer_matrix)))

current_row = 0
pivvot_index = []
for i in range(columns):

    search = False
    max = augmented_matrix[current_row:, i].argmax()
    j = augmented_matrix[current_row+max][i]
    if(j==0):
        max=augmented_matrix[current_row:,i].argmin()
        j=augmented_matrix[current_row+max][i]
    if (j != 0 ):
        pivvot_index.append(current_row * (columns + 1) + i)
        search = True
        if (current_row+max != current_row):
            temp = []
            for c in augmented_matrix[current_row]:
                temp.append(c)
            temp1 = []
            for c1 in augmented_matrix[current_row+max]:
                temp1.append(c1)
            augmented_matrix[current_row] = temp1
            augmented_matrix[current_row+max] = temp
        temp_row_2 = current_row + 1;
        for k in augmented_matrix[current_row + 1:, i]:
            if (k != 0):
                devide = -k / j
                temp_row_calculate = []
                for counter in augmented_matrix[current_row]:
                    temp_row_calculate.append(make_num_valid_calc(counter*devide))
                # print(temp_row_calculate)
                num = 0
                for counter1 in augmented_matrix[temp_row_2]:
                    augmented_matrix[temp_row_2][num] += temp_row_calculate[num]
                    make_num_valid(augmented_matrix,temp_row_2,num)
                    num += 1
                # print(augmented_matrix)
                # print('slm')
            temp_row_2 += 1
        culmn_calculator = 0
        # for s in augmented_matrix[current_row]:
        #     augmented_matrix[current_row][culmn_calculator] /= j
        #     culmn_calculator += 1

    if (search):
        current_row += 1


# // backward phase
for index in reversed(pivvot_index):
    pivot_row = index // (columns + 1)
    pivot_culmn = index % (columns + 1)
    curr_row = 0
    for row_num in augmented_matrix[0:pivot_row, pivot_culmn]:
        if (row_num != 0):
            devide = -row_num / augmented_matrix[pivot_row][pivot_culmn]
            # print(devide)
            temp_row_calculate = []
            for counter2 in augmented_matrix[pivot_row]:

                temp_row_calculate.append(make_num_valid_calc(counter2*devide))
            # print(temp_row_calculate)
            num = 0
            for counter1 in augmented_matrix[curr_row]:
                augmented_matrix[curr_row][num] += temp_row_calculate[num]
                make_num_valid(augmented_matrix, curr_row, num)
                num += 1

        curr_row += 1
    culmn_calculator = 0
    taghsim= augmented_matrix[pivot_row][pivot_culmn]
    for s in augmented_matrix[pivot_row]:
        augmented_matrix[pivot_row][culmn_calculator] /= taghsim
        culmn_calculator+=1

#find answers
pivot_columns=[]
for index in pivvot_index:
    pivot_columns.append(index%(columns+1))
    pivot_r=index//(columns+1)
    if(augmented_matrix[pivot_r][columns]==0):
        print('This system is inconsistent')
        exit(0)
answer={}
for aras in range(row):
    if(pivot_columns.count(aras)==0):
        answer.pop(aras,'free')


