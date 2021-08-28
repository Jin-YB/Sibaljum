# import Runcode # 파일간 연결

# result_data = Runcode.result_join
result_data = "노예와애예"  # 테스트용
data = list(result_data)  #

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

all_list = [[-1 for col_n in range(3)] for row_n in range(3)]

#  list_len = len(all_list)


""""
# all_list[A][B]
# [0][0]=한글.초성 [0][1]=한글.중성 [0][2]=한글.종성
# [1][0]=알파벳.대문자 [1][1]=알파벳.소문자
# [2][0]=아라비아 숫자 [2][1]=기호
# [3][a]=문법
"""


def uni_set():
    for i in range(count):
        uni_data.append(ord(data[i]))


def trans_uni_ko(seq):
    cho_uni.append((uni_data[seq] - 44032) // 588)  # 초성
    joong_uni.append(((uni_data[seq] - 44032) % 588) // 28)  # 중성
    jong_uni.append(((uni_data[seq] - 44032) % 588) % 28)  # 종성
    all_list[0][0] = cho_uni.pop()
    all_list[0][1] = joong_uni.pop()
    all_list[0][2] = jong_uni.pop()
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
    # jong_uni  (0~26)
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




