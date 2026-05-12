import numpy as np

def Move(numMove, pos, distance, lst_pos):
    row, col = pos[0] , pos[1]
    for i in range(1,distance+1):
        if numMove == 0:
            lst_pos.append([row,col+i])
        elif numMove == 1:
            lst_pos.append([row+i,col])
        elif numMove == 2:
            lst_pos.append([row,col-i])
        elif numMove == 3:
            lst_pos.append([row-i,col])
    return(lst_pos)



arr_map = np.array([[7,2,0,1,0,2,9],[8,4,8,6,9,3,3],[7,8,8,8,9,0,6],[4,7,2,7,0,0,7],[6,5,7,8,0,7,2],[8,1,8,5,4,5,2]])
print("Enter the point in form num1,num2.")
print("[1,2] must be 1,2 ")
pos_txt = input("Enter the point in form num1,num2 : ").split(",") 
pos_start = [int(pos_txt[0]),int(pos_txt[1])]
print(pos_start)



R, C = arr_map.shape[0]-1, arr_map.shape[1]-1
lst_pos = [pos_start]
r, c = pos_start[0], pos_start[1]
#create list distance 
lst_distance = [C-c,R-r,R+1,(R-1)-r,C-1]
i = 1
while True:
    lst_distance.append(lst_distance[i]-2)
    if lst_distance[-2]==1:
        break
    i += 1
# print(lst_distance)


#create list of point
for i in range(len(lst_distance)):
    Move(i%4,  lst_pos[-1], lst_distance[i], lst_pos)

# print(lst_pos)
for pos in lst_pos:
    print(arr_map[pos[0]][pos[1]], end=" ")