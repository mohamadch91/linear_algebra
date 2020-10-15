import numpy as np

print("enter row on column please\n>")
row = int(input())
columns = int(input())
zarayeb_matrix = []
for i in range(row):
    print("please enter row {} : \n>".format(i + 1))
    for j in range(columns):
        zarayeb_matrix.append(int(input()))

answer_matrix = []
print('enter constant values: \n >')
for i in range(row):
    answer_matrix.append(int(input()))
zarayeb_matrix = np.array(zarayeb_matrix).reshape(row, columns)
answer_matrix = np.array(answer_matrix).reshape(row, 1)
answer_matrix = np.array(answer_matrix[:, -1]).reshape(-1, 1)
augmented_matrix = np.hstack(((zarayeb_matrix, answer_matrix)))

current_row = 0

for i in range(columns-1):
    temp_row = current_row
    search = False
    for j in augmented_matrix[current_row:, i]:
        if (j != 0):
            search = True
            if (temp_row != current_row):
                temp = []
                for c in augmented_matrix[current_row]:
                    temp.append(c)
                temp1 = []
                for c1 in augmented_matrix[temp_row]:
                    temp1.append(c1)
                augmented_matrix[current_row] = temp1
                augmented_matrix[temp_row] = temp
            temp_row_2 = current_row + 1;
            for k in augmented_matrix[current_row + 1:, i]:
                if (k != 0):
                    devide = -k / j
                    temp_row_calculate = []
                    for counter in augmented_matrix[current_row]:
                        temp_row_calculate.append(counter * devide)
                    num = 0
                    for counter1 in augmented_matrix[temp_row_2]:
                        augmented_matrix[temp_row_2][num]+= temp_row_calculate[num]
                        num += 1

                temp_row_2 += 1
            culmn_calculator=0
            for s in augmented_matrix[current_row]:
                augmented_matrix[current_row][culmn_calculator]/=j
                culmn_calculator+=1;
            break

        temp_row += 1
    if (search):
        current_row += 1
print(augmented_matrix)