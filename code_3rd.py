#import Runcode # 파일간 연결

#result_data = Runcode.result_join
result_data="ㄱ ㅏ ㄱ" #테스트용
data = list(result_data) #

print(data)
uni_data = []
count = len(data)
cho_uni = []
joong_uni = []
jong_uni = []
eng_uni_c = []
eng_uni_s = []



def trans_uni_ko():

    for i in range(count):

        cho_uni.append((uni_data[i]-44032)//588)    # 초성
        joong_uni.append(((uni_data[i]-44032)%588)//28) #중성
        jong_uni.append(((uni_data[i]-44032)%588)%28)   #종성
        #  여기부터
        print(uni_data[i])
        print(cho_uni[i])
        print(joong_uni[i])
        print(jong_uni[i])
        #  여기까지 테스트용 출력
        #  출력시 저장되는 데이터 정보
        #  cho_uni (0~17){ 'ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'}
        #  joong_uni (0~20){'ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ'}
        #  jong_uni  (0~26){'\0', 'ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ', 'ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'}
def trans_uni_en_c():

    eng_uni_c.append(uni_data[i] - 65) # 대문자

def trans_uni_en_s():
    eng_uni_s.append(uni_data[i] - 97)  # 소문자


def start_data():
    for i in range(count):
        uni_data.append(ord(data[i])) # 글자데이터 >> 유니코드로 변환
    if  uni_data < (@@@) and uni_data >(@@@) # 유니코드 한글 범위
        trans_uni_ko()

    if  uni_data < (@@@) and uni_data >(@@@) # 유니코드 대문자 영어 범위
        trans_uni_en_c()
    if uni_data < (@ @ @) and uni_data > (@ @ @)  # 유니코드 소문자 영어 범위
        trans_uni_en_s()

start_data()