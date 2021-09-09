import code_3rd
import dot_data
import dot_data_eng
import circuit
import grm

idx_s = 0


def start_data(stk):
    global idx_s

    for i in range(4):
        for j in range(4):
            code_3rd.all_list[i][j] = -1
    dot_data.reset()
    code_3rd.uni_set()


    if 44032 <= code_3rd.uni_data[stk] <= 55203:  # 유니코드 한글 범위
        grm.grammar_10(stk)
        grm.grammar_11(stk)
        grm.grammar_12(stk)
        grm.grammar_18(stk)
        if 11 >= code_3rd.all_list[3][0] >= 1:  # 12항 가~하
            dot_data.grammar()
            circuit.play()
            for i in range(2):
                dot_data.reset()
                dot_data.jong(i)
                circuit.play()
            idx_s += 1
        elif 26 >= code_3rd.all_list[3][0] >= 12:  # 12항 억 ~ 것
            dot_data.cho()
            circuit.play()
            dot_data.reset()
            dot_data.grammar()
            circuit.play()
            code_3rd.trans_jong()
            dot_data.reset()
            dot_data.jong(1)
            circuit.play()
            idx_s += 1
        # 16항 예외적 경우 추가 해야함
        elif code_3rd.all_list[3][1] != -1:               # 18항
            dot_data.grammar()
            circuit.play()
            dot_data.reset()
            if code_3rd.all_list[3][1] == 0 or 1 or 2 or 4 or 5:
                idx_s += 3
            elif code_3rd.all_list[3][1] == 3 or 6:
                idx_s += 4
        else:
            code_3rd.trans_uni_ko(stk)
            code_3rd.trans_jong()
            dot_data.cho()
            circuit.play()
            dot_data.reset()
            print("초성\n")                              # 테스트용
            dot_data.joong()
            circuit.play()
            dot_data.reset()
            print("중성\n")                              # 테스트용
            for i in range(2):
                dot_data.reset()
                dot_data.jong(i)
                circuit.play()
            print("종성\n")                              # 테스트용
            dot_data.reset()
            if code_3rd.all_list[3][0] == 0:            # 10항 11항
                dot_data.grammar()
                circuit.play()
            idx_s += 1

    elif 65 <= code_3rd.uni_data[stk] <= 90:  # 유니코드 대문자 영어 범위
        code_3rd.trans_uni_en_c(stk)
        dot_data_eng.eng_c()
        circuit.play()
        print("대문자\n")                             # 테스트용
        dot_data.reset()
        idx_s += 1

    elif 97 <= code_3rd.uni_data[stk] <= 122:  # 유니코드 소문자 영어 범위
        code_3rd.trans_uni_en_s(stk)
        dot_data_eng.eng_s()
        circuit.play()
        print("소문자\n")                             # 테스트용
        dot_data.reset()
        idx_s += 1

    elif 48 <= code_3rd.uni_data[stk] <= 57:
        code_3rd.trans_uni_number(stk)
        dot_data_eng.number_()
        circuit.play()
        print("숫자\n")                               # 테스트용
        dot_data.reset()
        idx_s += 1

    else:
        code_3rd.trans_uni_sign(stk)
        dot_data_eng.sign()
        circuit.play()
        print("기호\n")                               # 테스트용
        dot_data.reset()
        idx_s += 1

print("시작")


while idx_s < code_3rd.count:
    if idx_s == code_3rd.count:
        break
    start_data(idx_s)
