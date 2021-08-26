import code_3rd


grammar_10_uni = []
grammar_10_count = [0] * code_3rd.count


def grammar_10():
    for i in range(code_3rd.count):
        grammar_10_uni.append(((code_3rd.uni_data[i] - 44032) % 588) % 28)
    a = 0


    # 제 10항 모음 + '예' 50696 모음
    while a < code_3rd.count:
        b = a + 1
        if code_3rd.count-1 == a:
            break

        if grammar_10_uni[a] == 0:
            if code_3rd.uni_data[b] == 50696:
                grammar_10_count[a] = 1
            else:
                grammar_10_count[a] = 0
        a += 1


"""
    if code_3rd.data[a] == 0:
        print(0)

"""

code_3rd.uni_set()
grammar_10()
# 테스트용
for i in range(code_3rd.count):
    if grammar_10_count[i] == 1:
        print(i)
    else:
        print("X")
        

