import code_3rd

stk = 0
dot = [[-1 for col_e in range(6)] for row_e in range(2)]
#  -1 은 초기값 (초기화)

"""
# 출력시 저장되는 데이터 정보
# cho_uni (0~18)
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
        dot[0][0] = 0             # 된소리표
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
    if code_3rd.all_list[0][0] == 2:       # ㄴ ={1 0 0 1 0 0}
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[0][0] == 3:       # ㄷ ={0 1 0 1 0 0}
        dot[0][0] = 0
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[0][0] == 4:  # ㄸ ={0 0 0 0 0 1} {0 1 0 1 0 0}
        dot[0][0] = 0             # 된소리표
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 1

        dot[1][0] = 0              # ㄷ
        dot[1][1] = 1
        dot[1][2] = 0
        dot[1][3] = 1
        dot[1][4] = 0
        dot[1][5] = 0
    if code_3rd.all_list[0][0] == 5:       # ㄹ ={0 1 0 1 0 0}
        dot[0][0] = 0
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[0][0] == 6:       # ㅁ ={1 0 0 0 1 0}
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[0][0] == 7:       # ㅂ ={0 0 0 1 1 0}
        dot[0][0] = 0
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[0][0] == 8:  # ㅃ ={0 0 0 0 0 1} {0 0 0 1 1 0}
        dot[0][0] = 0             # 된소리표
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 1

        dot[1][0] = 0              # ㅂ
        dot[1][1] = 0
        dot[1][2] = 0
        dot[1][3] = 1
        dot[1][4] = 1
        dot[1][5] = 0
    if code_3rd.all_list[0][0] == 9:       # ㅅ ={0 0 0 0 0 1}
        dot[0][0] = 0
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 1
    if code_3rd.all_list[0][0] == 10:  # ㅆ ={0 0 0 0 0 1} {0 0 0 0 0 1}
        dot[0][0] = 0             # 된소리표
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 1

        dot[1][0] = 0              # ㅅ
        dot[1][1] = 0
        dot[1][2] = 0
        dot[1][3] = 0
        dot[1][4] = 0
        dot[1][5] = 1
    if code_3rd.all_list[0][0] == 11:       # ㅇ ={1 1 0 1 1 0}(첫소리에 오면 생략가능?)
        dot[0][0] = 1
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[0][0] == 12:       # ㅈ ={0 0 0 1 0 1}
        dot[0][0] = 0
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 1
    if code_3rd.all_list[0][0] == 13:  # ㅉ ={0 0 0 0 0 1} {0 0 0 1 0 1}
        dot[0][0] = 0             # 된소리표
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 1

        dot[1][0] = 0              # ㅈ
        dot[1][1] = 0
        dot[1][2] = 0
        dot[1][3] = 1
        dot[1][4] = 0
        dot[1][5] = 1
    if code_3rd.all_list[0][0] == 14:       # ㅊ ={0 0 0 0 1 1}
        dot[0][0] = 0
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 1
        dot[0][5] = 1
    if code_3rd.all_list[0][0] == 15:       # ㅋ ={1 1 0 1 0 0}
        dot[0][0] = 1
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[0][0] == 16:       # ㅌ ={1 1 0 0 1 0}
        dot[0][0] = 1
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[0][0] == 17:       # ㅍ ={1 0 0 1 1 0}
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[0][0] == 18:       # ㅎ ={0 1 0 1 1 0}
        dot[0][0] = 0
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 0


def joong():
    if code_3rd.all_list[0][1] == 0:      # ㅏ ={1 1 0 0 0 1}
        dot[0][0] = 1
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 1
    if code_3rd.all_list[0][1] == 1:      # ㅐ ={1 1 1 0 1 0}
        dot[0][0] = 1
        dot[0][1] = 1
        dot[0][2] = 1
        dot[0][3] = 0
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[0][1] == 2:      # ㅑ ={0 0 1 1 1 0}
        dot[0][0] = 0
        dot[0][1] = 0
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[0][0] == 3:  # ㅒ ={0 0 1 1 1 0} {1 1 1 0 1 0}
        dot[0][0] = 0
        dot[0][1] = 0
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 0

        dot[1][0] = 1
        dot[1][1] = 1
        dot[1][2] = 1
        dot[1][3] = 0
        dot[1][4] = 1
        dot[1][5] = 0
    if code_3rd.all_list[0][1] == 4:      # ㅓ ={0 1 1 1 0 0}
        dot[0][0] = 0
        dot[0][1] = 1
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[0][1] == 5:      # ㅔ ={1 0 1 1 1 0}
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[0][1] == 6:      # ㅕ ={1 0 0 0 1 1}
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 1
        dot[0][5] = 1
    if code_3rd.all_list[0][1] == 7:      # ㅖ ={0 0 1 1 0 0}
        dot[0][0] = 0
        dot[0][1] = 0
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[0][1] == 8:      # ㅗ ={1 0 1 0 0 1}
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 1
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 1
    if code_3rd.all_list[0][1] == 9:      # ㅘ ={1 1 1 0 0 1}
        dot[0][0] = 1
        dot[0][1] = 1
        dot[0][2] = 1
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 1
    if code_3rd.all_list[0][0] == 10:  # ㅙ ={1 1 1 0 0 1} {1 1 1 0 1 0}
        dot[0][0] = 1
        dot[0][1] = 1
        dot[0][2] = 1
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 1

        dot[1][0] = 1
        dot[1][1] = 1
        dot[1][2] = 1
        dot[1][3] = 0
        dot[1][4] = 1
        dot[1][5] = 0
    if code_3rd.all_list[0][1] == 11:      # ㅚ ={1 0 1 1 1 1}
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 1
    if code_3rd.all_list[0][1] == 12:      # ㅛ ={0 0 1 1 0 1}
        dot[0][0] = 0
        dot[0][1] = 0
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 1
    if code_3rd.all_list[0][1] == 13:      # ㅜ ={1 0 1 1 0 0}
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[0][1] == 14:      # ㅝ ={1 1 1 1 0 0}
        dot[0][0] = 1
        dot[0][1] = 1
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[0][0] == 15:  # ㅞ ={1 1 1 1 0 0} {1 1 1 0 1 0}
        dot[0][0] = 1
        dot[0][1] = 1
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 0

        dot[1][0] = 1
        dot[1][1] = 1
        dot[1][2] = 1
        dot[1][3] = 0
        dot[1][4] = 1
        dot[1][5] = 0
    if code_3rd.all_list[0][0] == 16:  # ㅟ ={1 0 1 1 0 0} {1 1 1 0 1 0}
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 0

        dot[1][0] = 1
        dot[1][1] = 1
        dot[1][2] = 1
        dot[1][3] = 0
        dot[1][4] = 1
        dot[1][5] = 0
    if code_3rd.all_list[0][1] == 17:      # ㅠ ={1 0 0 1 0 1}
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 1
    if code_3rd.all_list[0][1] == 18:      # ㅡ ={0 1 0 1 0 1}
        dot[0][0] = 0
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 1
    if code_3rd.all_list[0][1] == 19:      # ㅢ ={0 1 0 1 1 1}
        dot[0][0] = 0
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 1
    if code_3rd.all_list[0][1] == 20:      # ㅣ ={1 0 1 0 1 0}
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 1
        dot[0][3] = 0
        dot[0][4] = 1
        dot[0][5] = 0


def jong(a):

    if code_3rd.all_list[0][a+2] == 0:        # (/0)
        dot[0][0] = -1
        dot[0][1] = -1
        dot[0][2] = -1
        dot[0][3] = -1
        dot[0][4] = -1
        dot[0][5] = -1
    if code_3rd.all_list[0][a+2] == 1:  # ㄱ
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[0][a+2] == 2:  # ㄴ
        dot[0][0] = 0
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[0][a+2] == 3:  # ㄷ
        dot[0][0] = 0
        dot[0][1] = 0
        dot[0][2] = 1
        dot[0][3] = 0
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[0][a+2] == 4:  # ㄹ
        dot[0][0] = 0
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[0][a+2] == 5:  # ㅁ
        dot[0][0] = 0
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 1
    if code_3rd.all_list[0][a+2] == 6:  # ㅂ
        dot[0][0] = 1
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[0][a+2] == 7:  # ㅅ
        dot[0][0] = 0
        dot[0][1] = 0
        dot[0][2] = 1
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[0][a+2] == 8:  # ㅇ
        dot[0][0] = 0
        dot[0][1] = 1
        dot[0][2] = 1
        dot[0][3] = 0
        dot[0][4] = 1
        dot[0][5] = 1
    if code_3rd.all_list[0][a+2] == 9:  # ㅈ
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 1
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[0][a+2] == 10:  # ㅊ
        dot[0][0] = 0
        dot[0][1] = 1
        dot[0][2] = 1
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[0][a+2] == 11:  # ㅋ
        dot[0][0] = 0
        dot[0][1] = 1
        dot[0][2] = 1
        dot[0][3] = 0
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[0][a+2] == 12:  # ㅌ
        dot[0][0] = 0
        dot[0][1] = 1
        dot[0][2] = 1
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 1
    if code_3rd.all_list[0][a+2] == 13:  # ㅍ
        dot[0][0] = 0
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 1
        dot[0][5] = 1
    if code_3rd.all_list[0][a+2] == 14:  # ㅎ
        dot[0][0] = 0
        dot[0][1] = 0
        dot[0][2] = 1
        dot[0][3] = 0
        dot[0][4] = 1
        dot[0][5] = 1
    if code_3rd.all_list[0][a+2] == 15:  # ㅆ
        dot[0][0] = 0
        dot[0][1] = 0
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 0


def reset():                    # 초기화
    for i in range(2):
        for j in range(6):
            dot[i][j] = -1


def grammar():
    if code_3rd.all_list[3][0] == 1:
        dot[0][0] = 1  # 가
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 1
    if code_3rd.all_list[3][0] == 2:
        dot[0][0] = 1  # 나
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[3][0] == 3:
        dot[0][0] = 0  # 다
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[3][0] == 4:
        dot[0][0] = 1  # 마
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[3][0] == 5:
        dot[0][0] = 0  # 바
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[3][0] == 6:
        dot[0][0] = 1  # 사
        dot[0][1] = 1
        dot[0][2] = 1
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[3][0] == 7:
        dot[0][0] = 0  # 자
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 1
    if code_3rd.all_list[3][0] == 8:
        dot[0][0] = 1  # 카
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 0
    if code_3rd.all_list[3][0] == 9:
        dot[0][0] = 1  # 타
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[3][0] == 10:
        dot[0][0] = 1  # 파
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[3][0] == 11:
        dot[0][0] = 0  # 하
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[3][0] == 12:
        dot[0][0] = 1  # 억
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 1
    if code_3rd.all_list[3][0] == 13:
        dot[0][0] = 0  # 언
        dot[0][1] = 1
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 1
    if code_3rd.all_list[3][0] == 14:
        dot[0][0] = 0  # 얼
        dot[0][1] = 1
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[3][0] == 15:
        dot[0][0] = 1  # 연
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 1
    if code_3rd.all_list[3][0] == 16:
        dot[0][0] = 1  # 열
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 1
        dot[0][5] = 1
    if code_3rd.all_list[3][0] == 17:
        dot[0][0] = 1  # 영
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 1
    if code_3rd.all_list[3][0] == 18:
        dot[0][0] = 1  # 옥
        dot[0][1] = 0
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 1
    if code_3rd.all_list[3][0] == 19:
        dot[0][0] = 1  # 온
        dot[0][1] = 1
        dot[0][2] = 1
        dot[0][3] = 0
        dot[0][4] = 1
        dot[0][5] = 1
    if code_3rd.all_list[3][0] == 20:
        dot[0][0] = 1  # 옹
        dot[0][1] = 1
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 1
    if code_3rd.all_list[3][0] == 21:
        dot[0][0] = 1  # 운
        dot[0][1] = 1
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[3][0] == 22:
        dot[0][0] = 1  # 울
        dot[0][1] = 1
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 1
    if code_3rd.all_list[3][0] == 23:
        dot[0][0] = 1  # 은
        dot[0][1] = 0
        dot[0][2] = 1
        dot[0][3] = 0
        dot[0][4] = 1
        dot[0][5] = 1
    if code_3rd.all_list[3][0] == 24:
        dot[0][0] = 0  # 을
        dot[0][1] = 1
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 0
        dot[0][5] = 1
    if code_3rd.all_list[3][0] == 25:
        dot[0][0] = 1  # 인
        dot[0][1] = 1
        dot[0][2] = 1
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 0
    if code_3rd.all_list[3][0] == 26:
        dot[0][0] = 0  # 것
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 1
        dot[0][4] = 1
        dot[0][5] = 1

        dot[1][0] = 0
        dot[1][1] = 1
        dot[1][2] = 1
        dot[1][3] = 1
        dot[1][4] = 0
        dot[1][5] = 0

    if code_3rd.all_list[3][1] == 0:  # 그래서
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 0

        dot[1][0] = 0
        dot[1][1] = 1
        dot[1][2] = 1
        dot[1][3] = 1
        dot[1][4] = 0
        dot[1][5] = 0
    if code_3rd.all_list[3][1] == 1:  # 그러나
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 0

        dot[1][0] = 1
        dot[1][1] = 0
        dot[1][2] = 0
        dot[1][3] = 1
        dot[1][4] = 0
        dot[1][5] = 0
    if code_3rd.all_list[3][1] == 2:  # 그러면
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 0

        dot[1][0] = 0
        dot[1][1] = 1
        dot[1][2] = 0
        dot[1][3] = 0
        dot[1][4] = 1
        dot[1][5] = 0
    if code_3rd.all_list[3][1] == 3:  # 그러므로
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 0

        dot[1][0] = 0
        dot[1][1] = 1
        dot[1][2] = 0
        dot[1][3] = 0
        dot[1][4] = 0
        dot[1][5] = 1
    if code_3rd.all_list[3][1] == 4:  # 그런데
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 0

        dot[1][0] = 1
        dot[1][1] = 0
        dot[1][2] = 1
        dot[1][3] = 1
        dot[1][4] = 1
        dot[1][5] = 0
    if code_3rd.all_list[3][1] == 5:  # 그리고
        dot[0][0] = 1
        dot[0][1] = 0
        dot[0][2] = 0
        dot[0][3] = 0
        dot[0][4] = 0
        dot[0][5] = 0

        dot[1][0] = 1
        dot[1][1] = 0
        dot[1][2] = 1
        dot[1][3] = 0
        dot[1][4] = 0
        dot[1][5] = 1
    if code_3rd.all_list[3][1] == 6:  # 그리하여
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
        dot[1][4] = 1
        dot[1][5] = 1
