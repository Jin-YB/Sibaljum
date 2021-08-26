import code_3rd
import dot_data


def eng_c():
    if code_3rd.all_list[1][0] == 0:
        dot_data.dot[0][0] = 0
        dot_data.dot[0][1] = 0
        dot_data.dot[0][2] = 0
        dot_data.dot[0][3] = 0
        dot_data.dot[0][4] = 0
        dot_data.dot[0][5] = 1

        dot_data.dot[1][0] = 1
        dot_data.dot[1][1] = 0
        dot_data.dot[1][2] = 0
        dot_data.dot[1][3] = 0
        dot_data.dot[1][4] = 0
        dot_data.dot[1][5] = 0


def eng_s():
    if code_3rd.all_list[1][1] == 0:
        dot_data.dot[0][0] = 1
        dot_data.dot[0][1] = 0
        dot_data.dot[0][2] = 0
        dot_data.dot[0][3] = 0
        dot_data.dot[0][4] = 0
        dot_data.dot[0][5] = 0



def number_():
    if code_3rd.all_list[2][0] == 0:
        dot_data.dot[0][0] = 0
        dot_data.dot[0][1] = 0
        dot_data.dot[0][2] = 1
        dot_data.dot[0][3] = 1
        dot_data.dot[0][4] = 1
        dot_data.dot[0][5] = 1

        dot_data.dot[1][0] = 1
        dot_data.dot[1][1] = 0
        dot_data.dot[1][2] = 0
        dot_data.dot[1][3] = 0
        dot_data.dot[1][4] = 0
        dot_data.dot[1][5] = 0


def sign():
    if code_3rd.all_list[2][1] == 44:
        dot_data.dot[0][0] = 0
        dot_data.dot[0][1] = 1
        dot_data.dot[0][2] = 0
        dot_data.dot[0][3] = 0
        dot_data.dot[0][4] = 0
        dot_data.dot[0][5] = 0
