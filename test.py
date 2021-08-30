import code_3rd
import dot_data
import dot_data_eng
import circuit
import grm

idx = 0


def start_data(stk):
    global idx

    for i in range(4):
        for j in range(4):
            code_3rd.all_list[i][j] = -1
    dot_data.reset()
    code_3rd.uni_set()
    grm.grammar_18(stk)
"""
# 출력시 저장되는 데이터 정보
# cho_uni (0~17)
{ 'ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'}
# joong_uni (0~20)
{'ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ'}
# jong_uni  (0~26)
{'\0', 'ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ', 'ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'}
"""


"""
# 테스트용
for i in range(code_3rd.count):
    if grammar_11_count[i] == 1:
        print(i)
    else:
        print("X")
"""