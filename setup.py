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
    grm.grammar_18(stk)
    if code_3rd.all_list[3][1] != -1:
        print("인덱스", idx_s)
        if code_3rd.all_list[3][1] == 0 or 1 or 2 or 4 or 5:
            idx_s += 3
        elif code_3rd.all_list[3][1] == 3 or 6:
            idx_s += 4
        else:
            idx_s += 1

    elif 44032 <= code_3rd.uni_data[stk] <= 55203:  # 유니코드 한글 범위
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
        print("인덱스", idx_s)
        idx_s += 1


    elif 65 <= code_3rd.uni_data[stk] <= 90:  # 유니코드 대문자 영어 범위
        code_3rd.trans_uni_en_c(stk)
        dot_data_eng.eng_c()
        circuit.play()
        print("대문자\n")                             # 테스트용
        dot_data.reset()
        print("인덱스", idx_s)
        idx_s += 1

    elif 97 <= code_3rd.uni_data[stk] <= 122:  # 유니코드 소문자 영어 범위
        code_3rd.trans_uni_en_s(stk)
        dot_data_eng.eng_s()
        circuit.play()
        print("소문자\n")                             # 테스트용
        dot_data.reset()
        print("인덱스", idx_s)
        idx_s += 1

    elif 48 <= code_3rd.uni_data[stk] <= 57:
        code_3rd.trans_uni_number(stk)
        dot_data_eng.number_()
        circuit.play()
        print("숫자\n")                               # 테스트용
        dot_data.reset()
        print("인덱스", idx_s)
        idx_s += 1

    else:
        code_3rd.trans_uni_sign(stk)
        dot_data_eng.sign()
        circuit.play()
        print("기호\n")                               # 테스트용
        dot_data.reset()
        print("인덱스", idx_s)
        idx_s += 1

print("시작")


while idx_s < code_3rd.count:
    idx_s = code_3rd.idx
    start_data(idx_s)
