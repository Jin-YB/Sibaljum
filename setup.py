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
            dot_data.joong()
            circuit.play()
            dot_data.jong()
            circuit.play()
            dot_data.reset()

        elif 65 <= code_3rd.uni_data[stk] <= 90:  # 유니코드 대문자 영어 범위
            code_3rd.trans_uni_en_c(stk)
            dot_data_eng.eng_c()
            circuit.play()

        elif 97 <= code_3rd.uni_data[stk] <= 122:  # 유니코드 소문자 영어 범위
            code_3rd.trans_uni_en_s(stk)
            dot_data_eng.eng_c()
            circuit.play()

        elif 48 <= code_3rd.uni_data[stk] <= 57:
            dot_data_eng.number()
            circuit.play()
        else:
            dot_data_eng.sign()
            circuit.play()
        stk += 1



start_data()
