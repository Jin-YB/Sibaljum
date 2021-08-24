result_data="안녕하세요"  # 안녕하세요는 샘플 이자리에 ocr 데이터 불러서 적용
data=list(result_data)
uni_data=[]
count=len(data)
cho_uni=[]
joong_uni=[]
jong_uni=[]




def trance_uni():
    for i in range(count):
        uni_data.append(ord(data[i]))  #안
        cho_uni.append((uni_data[i]-44032)//588)
        joong_uni.append(((uni_data[i]-44032)%588)//28)
        jong_uni.append(((uni_data[i]-44032)%588)%28)
        # 여기부터
        print(uni_data[i])
        print(cho_uni[i])
        print(joong_uni[i])
        print(jong_uni[i])
        # 여기까지 테스트용 출력


trance_uni()

#  출력시 저장되는 데이터 정보
#  cho_uni (0~17){ 'ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'}
#  joong_uni (0~20){'ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ'}
#  jong_uni  (0~26){'\0', 'ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ', 'ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'}