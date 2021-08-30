# import Runcode # 파일간 연결

# result_data = Runcode.result_join
result_data = "그리고가"  # 테스트용
data = list(result_data)  #
#{그리고세요}
# print(data)
uni_data = []
count = len(data)
cho_uni = []
joong_uni = []
jong_uni = []
eng_uni_c = []
eng_uni_s = []
num_uni = []
sign_uni = []
idx = 0
all_list = [[-1 for col_n in range(4)] for row_n in range(4)]

# list_len = len(all_list)


""""
# all_list[A][B]
# [0][0]=한글.초성 [0][1]=한글.중성 [0][2]=한글.종성 [0][3]=한글,종성
# [1][0]=알파벳.대문자 [1][1]=알파벳.소문자 [1][3]=한글.종성 더미박스
# [2][0]=아라비아 숫자 [2][1]=기호
# [3][0]=한글.글자 [3][1]=한글.단어 [3][2]=영어 [3][3]=숫자
"""


def uni_set():
    for i in range(count):
        uni_data.append(ord(data[i]))

def trans_jong():
    if all_list[1][3] == 0:
        all_list[0][1] = 0
        all_list[0][2] = 0
    if 1 <= all_list[1][3] <= 3:
        all_list[0][1] = 1
        if all_list[1][3] == 1:
            all_list[0][2] = 0
        elif all_list[1][3] == 2:
            all_list[0][2] = 1
        else:
            all_list[0][2] = 7
    if 4 <= all_list[1][3] <= 6:
        all_list[0][1] = 2
        if all_list[1][3] == 4:
            all_list[0][2] = 0
        elif all_list[1][3] == 5:
            all_list[0][2] = 9
        else:
            all_list[0][2] = 14
    if all_list[1][3] == 7:
        all_list[0][1] = 3
        all_list[0][2] = 0
    if 8 <= all_list[1][3] <= 15:
        all_list[0][1] = 4
        if all_list[1][3] == 8:
            all_list[0][2] = 0
        elif all_list[1][3] == 9:
            all_list[0][2] = 1
        elif all_list[1][3] == 10:
            all_list[0][2] = 5
        elif all_list[1][3] == 11:
            all_list[0][2] = 6
        elif all_list[1][3] == 12:
            all_list[0][2] = 7
        elif all_list[1][3] == 13:
            all_list[0][2] = 12
        elif all_list[1][3] == 14:
            all_list[0][2] = 13
        else:
            all_list[0][2] = 14
    if all_list[1][3] == 16:
        all_list[0][1] = 5
        all_list[0][2] = 0
    if 17 <= all_list[1][3] <= 18:
        all_list[0][1] = 6
        if all_list[1][3] == 14:
            all_list[0][2] = 0
        else:
            all_list[0][2] = 7
    if all_list[1][3] == 19:
        all_list[0][1] = 7
        all_list[0][2] = 0
    if all_list[1][3] == 20:
        all_list[0][1] = 15
        all_list[0][2] = 0
    if all_list[1][3] == 21:
        all_list[0][1] = 8
        all_list[0][2] = 0
    if all_list[1][3] == 22:
        all_list[0][1] = 9
        all_list[0][2] = 0
    if all_list[1][3] == 23:
        all_list[0][1] = 10
        all_list[0][2] = 0
    if all_list[1][3] == 24:
        all_list[0][1] = 11
        all_list[0][2] = 0
    if all_list[1][3] == 25:
        all_list[0][1] = 12
        all_list[0][2] = 0
    if all_list[1][3] == 26:
        all_list[0][1] = 13
        all_list[0][2] = 0
    if all_list[1][3] == 27:
        all_list[0][1] = 14
        all_list[0][2] = 0



def trans_uni_ko(seq):
    cho_uni.append((uni_data[seq] - 44032) // 588)  # 초성
    joong_uni.append(((uni_data[seq] - 44032) % 588) // 28)  # 중성
    jong_uni.append(((uni_data[seq] - 44032) % 588) % 28)  # 종성
    all_list[0][0] = cho_uni.pop()
    all_list[0][1] = joong_uni.pop()
    all_list[1][3] = jong_uni.pop()



    #  여기부터

    """
    print(uni_data[seq])
    print(cho_uni.pop())
    print(joong_uni.pop())
    print(jong_uni.pop())
    #  여기까지 테스트용 출력
    """

    """
    # 출력시 저장되는 데이터 정보
    # cho_uni (0~17)
    { 'ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'}
    # joong_uni (0~20)
    {'ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ'}
    # jong_uni  (0~27)
    {'\0', 'ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ', 'ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'}
    """

def trans_uni_en_c(seq):
    eng_uni_c.append(uni_data[seq] - 65)  # 대문자
    #  print(eng_uni_c.pop())
    all_list[1][0] = eng_uni_c.pop()


def trans_uni_en_s(seq):
    eng_uni_s.append(uni_data[seq] - 97)  # 소문자
    #  print(eng_uni_s.pop())
    all_list[1][1] = eng_uni_s.pop()


def trans_uni_number(seq):
    num_uni.append(uni_data[seq] - 48)   # 숫자
    all_list[2][0] = num_uni.pop()


def trans_uni_sign(seq):
    sign_uni.append(uni_data[seq])
    all_list[2][1] = sign_uni.pop()




