import numpy as np
from matplotlib import image as img
import matplotlib.pyplot as plt
""" in this program we make bigger  picture because 
if shear constant is big enough to shadow form get out of border of input picture
 make bigger picture to handle this problem
 and its feature :))
"""
#define shear constant to transform

shear_constant=float(input("Please enter shear constant(suggested : between 0.02 and 0.1 ) : "))
#transform y to new location with shear transform
def shear(x,y):
    return int(y+x*shear_constant)
#get image location from user and convert it into atrix
def getImage():
    user_input=input("PLease Enter Directori : ")
    # convert to matrix
    image_date=img.imread(user_input)
    return image_date
#make shadow matrix
def shadow_matrix(row,column):
    #new matrix with added column to show complete image
    column_s=int(column+column*shear_constant)
    #make shadow matrix with black baground
    shadow=np.zeros((row,column_s,3),dtype='uint8')
    #convert it to white back ground
    for i in range(row):
        for j in range(column_s):
            shadow[i][j]=(255,255,255)
    #make pixels shadow  and use shear transform to make it extensive
    for i in range (row):
        for j in range(column):
            #check if not white transform it
            if(user_input[i][j][0]<245 or user_input[i][j][1]<245 or user_input[i][j][2]<245 ):
                 shadow[i][shear(i,j)]=(80,80,80)
    return shadow
#merge shadow matrix and main one
def merge(shadow,input,row,column):
    columns=int(column+column*shear_constant)
    #make new matrix with black background
    final=np.zeros((row,columns,3),dtype='uint8')
    for i in range(row):
        for j in range(columns):
            #check for main matrix and use push main picture in final one
            if(j<column):
                #if background isn't white use main one
                if(input[i][j][0]<245 or input[i][j][1]<245 or input[i][j][2]<245):
                    final[i][j]=input[i][j]
                else:
                    #else use shadow form matrix
                    final[i][j]=shadow[i][j]
            else:
                #at the end complete matrix with end of shadow form
                final[i][j]=shadow[i][j]
    return final
if __name__ == "__main__":
    #get input and convert to matrix
    user_input=getImage()
    #get row and column of picture
    row,column,dim=user_input.shape
    #make shadow matrix
    shadow_img=shadow_matrix(row,column)
    #merge two matrixes
    final_img=merge(shadow_img,user_input,row,column)
    plt.imshow(final_img)
    plt.show()

