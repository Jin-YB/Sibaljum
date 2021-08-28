import code_3rd


code_3rd.uni_set()
grammar_15_uni1 = []
grammar_15_uni2 = []
grammar_15_count = []
def grammar_15():
    for i in range(code_3rd.count):
        grammar_15_uni1.append(((code_3rd.uni_data[i] - 44032) % 588) // 28)  # 중성
        grammar_15_uni2.append(((code_3rd.uni_data[i] - 44032) % 588) % 28)  # 종성
    a = 0

    while a < code_3rd.count:
        b = a + 1
        if code_3rd.count - 1 == a:
            break

        if grammar_15_uni1[a] == 4: # ㅓ
            if grammar_15_uni2[a] == 1: # ㄱ
                grammar_15_count[a] = 1
            elif grammar_15_uni2[a] == 4: # ㄴ
                grammar_15_count[a] = 2
            elif grammar_15_uni2[a] == 8: # ㄹ
                grammar_15_count[a] = 3
            else:
                grammar_15_count[a] = 0
        elif grammar_15_uni1[a] == 7:  # ㅕ
            if grammar_15_uni2[a] == 4:  # ㄴ
                grammar_15_count[a] = 4
            elif grammar_15_uni2[a] == 8:  # ㄹ
                grammar_15_count[a] = 5
            elif grammar_15_uni2[a] == 21:  # ㅇ
                grammar_15_count[a] = 6
            else:
                grammar_15_count[a] = 0
        else:
            grammar_15_count[a] = 0
        a += 1




"""

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