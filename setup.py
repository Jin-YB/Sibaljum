import code_3rd
import dot_data
import circuit

def start_data():
    code_3rd.uni_set()
    stk = 0
    while stk < code_3rd.count:

        if 44032 <= code_3rd.uni_data[stk] <= 55203:  # 유니코드 한글 범위
            code_3rd.trans_uni_ko(stk)
            dot_data.cho()
            dot_data.joong()
            dot_data.jong()
            circuit.play(stk)

        if 65 <= code_3rd.uni_data[stk] <= 90:  # 유니코드 대문자 영어 범위
            code_3rd.trans_uni_en_c(stk)

        if 97 <= code_3rd.uni_data[stk] <= 122:  # 유니코드 소문자 영어 범위
            code_3rd.trans_uni_en_s(stk)

        stk += 1


start_data()
