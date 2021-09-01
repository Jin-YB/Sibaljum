import dot_data
import time

delay = 5  # 딜레이 시간
# 임시 회로 시뮬레이터
def play():
    for i in range(2):
        for j in range(6):
            if dot_data.dot[i][j] == 1:
                print("D")
            elif dot_data.dot[i][j] == 0:
                print("I")

    dot_data.reset()

    time.sleep(delay)
    print("")



