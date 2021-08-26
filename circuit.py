import dot_data
import dot_data_eng
import time

delay = 0.01  # 딜레이 시간

def play(seq):
    for i in range(6):
        if dot_data.dot_cho[seq][i] == 1:
            print("D")
        elif dot_data.dot_cho[seq][i] == 0:
            print("I")

        if dot_data.dot_joong[seq][i] == 1:
            print("D")
        elif dot_data.dot_joong[seq][i] == 0:
            print("I")

        if dot_data.dot_jong[seq][i] == 1:
            print("D")
        elif dot_data.dot_jong[seq][i] == 0:
            print("I")

        if dot_data_eng.dot_eng_c[seq][i] == 1:
            print("D")
        elif dot_data_eng.dot_eng_c[seq][i] == 0:
            print("I")

        if dot_data_eng.dot_eng_s[seq][i] == 1:
            print("D")
        elif dot_data_eng.dot_eng_s[seq][i] == 0:
            print("I")

        if dot_data_eng.dot_number[seq][i] == 1:
            print("D")
        elif dot_data_eng.dot_number[seq][i] == 0:
            print("I")

    time.sleep(delay)

