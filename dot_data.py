import code_3rd

stk=0
dot = [[-1 for col_e in range(6)] for row_e in range(2)]
#  -1 은 초기값 (초기화)

"""
# 출력시 저장되는 데이터 정보
# cho_uni (0~17)
{ 'ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'}
# joong_uni (0~20)
{'ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ'}
# jong_uni  (0~26)
{'\0', 'ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ', 'ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'}
"""


def cho():
    if code_3rd.all_list[0][0] == 0:       # ㄱ ={0 0 0 1 0 0}
        dot[0][0] = 0
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[0][0] == 1:  # ㄲ ={0 0 0 0 0 1} {0 0 0 1 0 0}
        dot[0][0] = 0           # 된소리표
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 1

        dot[1][0] = 0              # ㄱ
        dot[1][1] = 0
        dot[1][2] = 0
        dot[1][3] = 1
        dot[1][4] = 0
        dot[1][5] = 0


def joong():
    if code_3rd.all_list[0][1] == 0:      # ㅏ ={1 1 0 0 0 1}
        dot[0][0] = 1
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 1


def jong():
    if code_3rd.all_list[0][2] == 0:        # (/0) ={0 0 0 0 0 0}
        dot[0][0] = -1
        dot[0][1] = -1
        dot[0][2] = -1
        dot[0][3] = -1
        dot[0][4] = -1
        dot[0][5] = -1
    
    if code_3rd.all_list[0][2] == 1:  # ㄱ ={1 0 0 0 0 0}
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 0

    if code_3rd.all_list[0][2] == 2:  # ㄲ ={1 0 0 0 0 0} {1 0 0 0 0 0}
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 0

        dot[1][0] = 1
        dot[1][1] = 0
        dot[1][2] = 0
        dot[1][3] = 0
        dot[1][4] = 0
        dot[1][5] = 0


def reset():                    # 초기화
    for i in range(2):
        for j in range(6):
            dot[i][j] = -1


"""while (stk < code_3rd.count):
    cho()
    joong()
    jong()
    for i in dot:                  #테스트용 출력
        for j in i:
            print(j, end=" ")
        print()
    print("\n")
    stk += 1
    reset() """

