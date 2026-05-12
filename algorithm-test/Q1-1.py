import numpy as np

arr_map = np.array([[7,2,0,1,0,2,9],[8,4,8,6,9,3,3],[7,8,8,8,9,0,6],[4,7,2,7,0,0,7],[6,5,7,8,0,7,2],[8,1,8,5,4,5,2]])

lst_pos = []
h = arr_map.shape[0]
w = arr_map.shape[1]

for j in range(w):
    if j%2 == 0:
        for i in range(0,h,1):  #ทิศลง
            lst_pos.append([i,j])
    else:
        for i in range(h-1,-1,-1): #ทิศขึ้น
            lst_pos.append([i,j])

for pos in lst_pos:
    print(arr_map[pos[0]][pos[1]], end=" ")