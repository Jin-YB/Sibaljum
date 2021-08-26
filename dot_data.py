import code_3rd

stk = 0
dot_cho = [[2 for col_e in range(6)] for row_e in range(2)]
dot_joong = [[2 for col_m in range(6)] for row_m in range(2)]
dot_jong = [[2 for col_f in range(6)] for row_f in range(2)]


#  출력시 저장되는 데이터 정보
#  cho_uni (0~17){ 'ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'}
#  joong_uni (0~20){'ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ'}
#  jong_uni  (0~26){'\0', 'ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ', 'ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ',
#  'ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'}

# 초성 출력


def cho():
    if code_3rd.cho_uni[stk] == 0:  # ㄱ ={0 0 0 1 0 0}
        dot_cho[0][0] = 0
        dot_cho[0][1] = 0
        dot_cho[0][2] = 0
        dot_cho[0][3] = 1
        dot_cho[0][4] = 0
        dot_cho[0][5] = 0
    if code_3rd.cho_uni[stk] == 1:  # ㄲ ={0 0 0 0 0 1} {0 0 0 1 0 0}
        dot_cho[0][0] = 0           # 된소리표
        dot_cho[0][1] = 0
        dot_cho[0][2] = 0
        dot_cho[0][3] = 0
        dot_cho[0][4] = 0
        dot_cho[0][5] = 1

        dot_cho[1][0] = 0              #    ㄱ
        dot_cho[1][1] = 0
        dot_cho[1][2] = 0
        dot_cho[1][3] = 1
        dot_cho[1][4] = 0
        dot_cho[1][5] = 0


def joong():
    if code_3rd.joong_uni[stk] == 0:      #  ㅏ ={1 1 0 0 0 1}
        dot_joong[0][0] = 1
        dot_joong[0][1] = 1
        dot_joong[0][2] = 0
        dot_joong[0][3] = 0
        dot_joong[0][4] = 0
        dot_joong[0][5] = 1


def jong():
    if code_3rd.jong_uni[stk] == 0:        #   (/0) ={0 0 0 0 0 0}
        dot_jong[0][0] = 0
        dot_jong[0][1] = 0
        dot_jong[0][2] = 0
        dot_jong[0][3] = 0
        dot_jong[0][4] = 0
        dot_jong[0][5] = 0
    
    if code_3rd.jong_uni[stk]==1: #ㄱ ={0 0 0 1 0 0}
        dot_jong[0][0] = 0
        dot_jong[0][1] = 0
        dot_jong[0][2] = 0
        dot_jong[0][3] = 1
        dot_jong[0][4] = 0
        dot_jong[0][5] = 0
    if code_3rd.jong_uni[stk] == 2: #ㄲ ={1 0 0 0 0 0} {1 0 0 0 0 0}
        dot_jong[0][0] = 1
        dot_jong[0][1] = 0
        dot_jong[0][2] = 0
        dot_jong[0][3] = 0
        dot_jong[0][4] = 0
        dot_jong[0][5] = 0

        dot_jong[1][0] = 1
        dot_jong[1][1] = 0
        dot_jong[1][2] = 0
        dot_jong[1][3] = 0
        dot_jong[1][4] = 0
        dot_jong[1][5] = 0


def reset():                    #초기화
    for i in range(2):
        for j in range(6):
            dot_cho[i][j] = 2
            dot_joong[i][j] = 2
            dot_jong[i][j] = 2

while (stk < code_3rd.count):
    cho()
    joong()
    jong()
    for i in dot_cho:                  #테스트용 출력
        for j in i:
            print(j, end=" ")
        print()
    print("\n")
    for i in dot_joong:
        for j in i:
            print(j, end=" ")
        print()
    print("\n")
    for i in dot_jong:
        for j in i:
            print(j, end=" ")
        print()
    print("\n")
    stk += 1
    reset()

