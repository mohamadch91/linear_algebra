import numpy as np
import math
# valid nums out put
def make_num_valid(matrix, row, column):
    num = matrix[row, column]
    if math.ceil(num) - num < 0.00000000001:
        matrix[row, column] = math.ceil(num)
    elif  num - math.floor(num)<0.00000000001:
      matrix[row,column]=math.floor(num)
def make_num_valid_calc(num):

    if math.ceil(num) - num < 0.00000000001:
        num=math.ceil(num)
    elif num - math.floor(num) < 0.00000000001:
        num = math.floor(num)
    return num

np.set_printoptions(3,suppress=True)
#input raws and columns
rows_columns=input("enter row on column please\n>").split()
row =int(rows_columns[0])
columns = int(rows_columns[1])
coefficient_matrix = []
for i in range(row):
    x=input("please enter row {} : \n>".format(i + 1)).split()
    for j in range(columns):
        coefficient_matrix.append(float(x[j]))
answer_matrix = []
constant_value=input('enter constant values: \n >').split()
#add constatnt value to matrix and re shape it
for i in range(row):
    answer_matrix.append(float(constant_value[i]))
coefficient_matrix = np.array(coefficient_matrix).reshape(row, columns)
answer_matrix = np.array(answer_matrix).reshape(row, 1)
answer_matrix = np.array(answer_matrix[:, -1]).reshape(-1, 1)
augmented_matrix = np.hstack(((coefficient_matrix, answer_matrix)))
print("Given matrix: {}".format(augmented_matrix))
#search for pivots and make undre rows zero
current_row = 0
pivvot_index = []
for i in range(columns):
    search = False
    #pivot in raw
    max = augmented_matrix[current_row:, i].argmax()
    j = augmented_matrix[current_row+max][i]
    #if do not  have positive pivot in raw
    if(j==0):
        max=augmented_matrix[current_row:,i].argmin()
        j=augmented_matrix[current_row+max][i]
    #if  have any pivot in raw
    if (j != 0 ):
        #save index of pivot
        pivvot_index.append(current_row * (columns + 1) + i)
        search = True
        #change rows if pivoy noy in first row
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
        #make under rows of pivot position  zero
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

            temp_row_2 += 1
    if (search):
        current_row += 1
# // backward phase
for index in reversed(pivvot_index):
    pivot_row = index // (columns + 1)
    pivot_column = index % (columns + 1)
    curr_row = 0
    for row_num in augmented_matrix[0:pivot_row, pivot_column]:
        # make zero upper rows in column
        if (row_num != 0):
            devide = -row_num / augmented_matrix[pivot_row][pivot_column]

            temp_row_calculate = []
            for counter2 in augmented_matrix[pivot_row]:

                temp_row_calculate.append(make_num_valid_calc(counter2*devide))

            num = 0
            for counter1 in augmented_matrix[curr_row]:
                augmented_matrix[curr_row][num] += temp_row_calculate[num]
                make_num_valid(augmented_matrix, curr_row, num)
                num += 1

        curr_row += 1
    column_calculator = 0
    taghsim= augmented_matrix[pivot_row][pivot_column]
    for s in augmented_matrix[pivot_row]:
        augmented_matrix[pivot_row][column_calculator] /= taghsim
        column_calculator+=1
#find answers
for m in range(row):
    #check system in consistent
    counter=0
    for s in range(columns):
        if(augmented_matrix[m][s]==0):
            counter+=1
    if(counter==columns and augmented_matrix[m][columns]!=0):
        print(" this system is inconsistent")
        exit(0)

pivot_columns=[]
for index in pivvot_index:
    pivot_columns.append(index%(columns+1))

answer={}
all_ans=[]
#add free answers
for aras in range(columns):
    # if column has no pivot its answer is free
    if(pivot_columns.count(aras)==0):
        answer[str(aras+1)]='is free'
        all_ans.append(aras+1)
        all_ans.append('is free')
# print(answer)
for index1 in reversed(pivvot_index):
    pivot_row=index1//(columns+1)
    pivot_columns=index1%(columns+1)
    ans=augmented_matrix[pivot_row][columns]
    ans=make_num_valid_calc(ans)
    temp_ans=''
    final_ans=''
    all_ans.append(pivot_columns+1)
    for s in range(pivot_columns+1,columns):
        if(augmented_matrix[pivot_row][s]==0):
            continue
        else:
            if(answer.get(str(s+1))=='is free'):
                temp_ans+='('+str((-1)*augmented_matrix[pivot_row][s])+'*X'+str(s+1)+')'
    if(ans==0):
        final_ans +=  temp_ans
    else:
        final_ans+=str(ans)+'+'+temp_ans
    all_ans.append(final_ans)

for kia in range(columns):
    x=all_ans.index(kia+1)
    final='X'+str(kia+1)+': '+all_ans[x+1]+'\n'
    print(final)
print("row reduced echolen form is : {}",augmented_matrix)



