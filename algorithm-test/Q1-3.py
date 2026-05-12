import numpy as np

arr_map = np.array([[7,2,0,1,0,2,9],[8,4,8,6,9,3,3],[7,8,8,8,9,0,6],[4,7,2,7,0,0,7],[6,5,7,8,0,7,2],[8,1,8,5,4,5,2]])

h , w = arr_map.shape[0]-1, arr_map.shape[1]-1


lst_allpool = []
check_duplicate = []

pos_start_target = [2,8]

h = len(arr_map)
w = len(arr_map[0])

for i in range(len(arr_map)):
    for j in range(len(arr_map[i])):

        pos_now = [i,j]
        num_target = pos_start_target[1]

        if arr_map[i][j] == pos_start_target[0]:

            lst_pos_target = []

            # WEST
            direction = 'W'

            for col in range(pos_now[1]-1,-1,-1):

                if arr_map[pos_now[0]][col] == num_target :
                    lst_pos_target.append([pos_now[0], col])
                    break

            if lst_pos_target != []:

                for pos in lst_pos_target:

                    txt_numPass = ""
                    count = 0

                    for col in range(pos_now[1],pos[1]-1,-1):

                        if col == pos[1]:
                            txt_numPass += str(arr_map[pos_now[0]][col])
                            count +=1
                        else:
                            txt_numPass += str(arr_map[pos_now[0]][col]) + ","
                            count +=1

                    txt_save = f"{direction} {txt_numPass}"

                    if txt_save not in check_duplicate:
                        check_duplicate.append(txt_save)
                        lst_allpool.append([count, txt_save])

                lst_pos_target = []


            # NORTH
            direction = 'N'

            for row in range(pos_now[0]-1,-1,-1):

                if arr_map[row][pos_now[1]] == num_target :
                    lst_pos_target.append([row, pos_now[1]])
                    break

            if lst_pos_target != []:

                for pos in lst_pos_target:

                    txt_numPass = ""
                    count = 0

                    for row in range(pos_now[0], pos[0]-1 ,-1):

                        if row == pos[0]:
                            txt_numPass += str(arr_map[row][pos_now[1]])
                            count +=1
                        else:
                            txt_numPass += str(arr_map[row][pos_now[1]]) + ","
                            count +=1

                    txt_save = f"{direction} {txt_numPass}"

                    if txt_save not in check_duplicate:
                        check_duplicate.append(txt_save)
                        lst_allpool.append([count, txt_save])

                lst_pos_target = []


            # SOUTH
            direction = 'S'

            for row in range(pos_now[0]+1,h):

                if arr_map[row][pos_now[1]] == num_target :
                    lst_pos_target.append([row, pos_now[1]])
                    break

            if lst_pos_target != []:

                for pos in lst_pos_target:

                    txt_numPass = ""
                    count = 0

                    for row in range(pos_now[0], pos[0]+1 ,1):

                        if row == pos[0]:
                            txt_numPass += str(arr_map[row][pos_now[1]])
                            count +=1
                        else:
                            txt_numPass += str(arr_map[row][pos_now[1]]) + ","
                            count +=1

                    txt_save = f"{direction} {txt_numPass}"

                    if txt_save not in check_duplicate:
                        check_duplicate.append(txt_save)
                        lst_allpool.append([count, txt_save])

                lst_pos_target = []


            # EAST
            direction = 'E'

            for col in range(pos_now[1]+1,w):

                if arr_map[pos_now[0]][col] == num_target :
                    lst_pos_target.append([pos_now[0], col])
                    break

            if lst_pos_target != []:

                for pos in lst_pos_target:

                    txt_numPass = ""
                    count = 0

                    for col in range(pos_now[1],pos[1]+1,1):

                        if col == pos[1]:
                            txt_numPass += str(arr_map[pos_now[0]][col])
                            count +=1
                        else:
                            txt_numPass += str(arr_map[pos_now[0]][col]) + ","
                            count +=1

                    txt_save = f"{direction} {txt_numPass}"

                    if txt_save not in check_duplicate:
                        check_duplicate.append(txt_save)
                        lst_allpool.append([count, txt_save])


shortest = min(lst_allpool)
longest = max(lst_allpool)

for item in lst_allpool:

    txt = item[1]

    if item == shortest:
        txt += " SHORTEST"

    elif item == longest:
        txt += " LONGEST"

    print(txt)