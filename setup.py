import code_3rd
import dot_data
import dot_data_eng
import circuit

def start_data():
    code_3rd.uni_set()
    stk = 0
    while stk < code_3rd.count:

        if 44032 <= code_3rd.uni_data[stk] <= 55203:  # 유니코드 한글 범위
            code_3rd.trans_uni_ko(stk)
            dot_data.cho()
            circuit.play()
            print("초성\n")                              # 테스트용
            dot_data.joong()
            circuit.play()
            print("중성\n")                              # 테스트용
            dot_data.jong()
            circuit.play()
            print("종성\n")                              # 테스트용
            dot_data.reset()

        elif 65 <= code_3rd.uni_data[stk] <= 90:  # 유니코드 대문자 영어 범위
            code_3rd.trans_uni_en_c(stk)
            dot_data_eng.eng_c()
            circuit.play()
            print("대문자\n")                             # 테스트용
            dot_data.reset()

        elif 97 <= code_3rd.uni_data[stk] <= 122:  # 유니코드 소문자 영어 범위
            code_3rd.trans_uni_en_s(stk)
            dot_data_eng.eng_s()
            circuit.play()
            print("소문자\n")                             # 테스트용
            dot_data.reset()

        elif 48 <= code_3rd.uni_data[stk] <= 57:
            code_3rd.trans_uni_number(stk)
            dot_data_eng.number_()  
            circuit.play()
            print("숫자\n")                               # 테스트용
            dot_data.reset()

        else:
            code_3rd.trans_uni_sign(stk)
            dot_data_eng.sign()
            circuit.play()
            print("기호\n")                               # 테스트용
            dot_data.reset()

        stk += 1



start_data()
