import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('noisy.jpg')
# print (img)
# print (img.shape)
R, G, B = img[:, :,0], img[ :, :,1], img[ :, :,2]

UR, SR, VR = np.linalg.svd(R)
UG, SG, VG = np.linalg.svd(G)
UB, SB, VB = np.linalg.svd(B)
SR_new=np.zeros((UR.shape[0],VR.shape[1]),dtype=int)
SG_new=np.zeros((UG.shape[0],VG.shape[1]),dtype=int)
SB_new=np.zeros((UB.shape[0],VB.shape[1]),dtype=int)

for m  in range(SR_new.shape[0]):
    for s in range (SR_new.shape[1]):
        if(m==s and m<=45):
            SR_new[m][s]=SR[m]

for m in range(SG_new.shape[0]):
    for s in range(SG_new.shape[1]):
        if (m == s and m <= 45):
            SG_new[m][s] =SG[m]

for m in range(SB_new.shape[0]):
    for s in range(SB_new.shape[1]):
        if (m == s and m <= 45):
            SB_new[m][s] = SB[m]

new_R=UR.dot(SR_new).dot(VR)
new_G=UG.dot(SG_new).dot(VG)
new_B=UB.dot(SB_new).dot(VB)
for s in range (new_R.shape[0]):
    for k in range (new_R.shape[1]):
        new_R[s][k]=int(new_R[s][k])

for s in range(new_G.shape[0]):
    for k in range(new_G.shape[1]):
        new_G[s][k] = int(new_G[s][k])

for s in range(new_B.shape[0]):
    for k in range(new_B.shape[1]):
        new_B[s][k] = int(new_B[s][k])
new_img=np.zeros((img.shape[0],img.shape[1],img.shape[2]),dtype=int)
new_img[:,:,0],new_img[:,:,1],new_img[:,:,2],=new_R,new_G,new_B
plt.imshow(new_img)
plt.show()






