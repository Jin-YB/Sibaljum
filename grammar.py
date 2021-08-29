import code_3rd

grammar_10_uni = []
grammar_10_count = [0] * code_3rd.count
grammar_11_uni1 = []
grammar_11_count = [0] * code_3rd.count
grammar_18_uni = [0] * code_3rd.count


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
            if 50726 >= code_3rd.uni_data[b] >= 50696:
                grammar_10_count[a] = 1
            else:
                grammar_10_count[a] = 0
        a += 1


def grammar_11():
    # 제 11항 모음(ㅑ,ㅘ,ㅜ,ㅝ) + '애' 50528 모음
    for i in range(code_3rd.count):
        grammar_11_uni1.append(((code_3rd.uni_data[i] - 44032) % 588) % 28)

    a = 0
    while a < code_3rd.count:
        b = a + 1
        if code_3rd.count - 1 == a:
            break

        if grammar_11_uni1[a] == 0:
            for i in range(24):
                if code_3rd.uni_data[a] == (44088 + (588 * i)) or code_3rd.uni_data[a] == (44284 + (588 * i)) or \
                        code_3rd.uni_data[a] == (44396 + (588 * i)) or code_3rd.uni_data[a] == (44424 + (588 * i)):
                    if 50555 >= code_3rd.uni_data[b] >= 50528:  # 애 ~ 앻
                        grammar_11_count[a] = 1
                    else:
                        grammar_11_count[a] = 0
        a += 1


""" 시작 글자 -> 그 """   # 앞자리 비었을때로 예외처리, all_list로 순서 정하기


def grammar_18():
    for j in range(code_3rd.count):
        grammar_18_uni.append(code_3rd.uni_data[i])
    a = 0
    while a < code_3rd.count-3:
        if a == 0:   # 처음시작(빈공간 당연히 x)
            if grammar_18_uni[a] == 44536:   # "그"
                if grammar_18_uni[a+1] == 47000:    # "래"
                    if grammar_18_uni[a+2] == 49436:    # 그래서
                        code_3rd.all_list[3][0] = 0
                        a += 2
                elif grammar_18_uni[a+1] == 47084:    # "러"
                    if grammar_18_uni[a+2] == 45208:   # 그러나
                        code_3rd.all_list[3][0] = 1
                        a += 2
                    elif grammar_18_uni[a+2] == 47732:   # 그러면
                        code_3rd.all_list[3][0] = 2
                        a += 2
                    elif grammar_18_uni[a+2] == 48064:   # "므"
                        if grammar_18_uni[a+3] == 47196:   # 그러므로
                            code_3rd.all_list[3][0] = 3
                            a += 3
                elif grammar_18_uni[a+1] == 47088:   # "런"
                    if grammar_18_uni[a+2] == 45936:   # 그런데
                        code_3rd.all_list[3][0] = 4
                        a += 2
                elif grammar_18_uni[a+1] == 47532:   # "리"
                    if grammar_18_uni[a+2] == 44256:   # 그리고
                        code_3rd.all_list[3][0] = 5
                        a += 2
                    elif grammar_18_uni[a+2] == 54616:   # "하"
                        if grammar_18_uni[a+3] == 50668:   # 그리하여
                            code_3rd.all_list[3][0] = 6
                            a += 3
        else:  # 앞에 공간이 있을 때
            if grammar_18_uni[a-1] == 32:  # 앞이 공백일 경우
                if grammar_18_uni[a] == 44536:  # "그"
                    if grammar_18_uni[a + 1] == 47000:  # "래"
                        if grammar_18_uni[a + 2] == 49436:  # 그래서
                            code_3rd.all_list[3][0] = 0
                            a += 3
                    elif grammar_18_uni[a + 1] == 47084:  # "러"
                        if grammar_18_uni[a + 2] == 45208:  # 그러나
                            code_3rd.all_list[3][0] = 1
                            a += 2
                        elif grammar_18_uni[a + 2] == 47732:  # 그러면
                            code_3rd.all_list[3][0] = 2
                            a += 2
                        elif grammar_18_uni[a + 2] == 48064:  # "므"
                            if grammar_18_uni[a + 3] == 47196:  # 그러므로
                                code_3rd.all_list[3][0] = 3
                                a += 3
                    elif grammar_18_uni[a + 1] == 47088:  # "런"
                        if grammar_18_uni[a + 2] == 45936:  # 그런데
                            code_3rd.all_list[3][0] = 4
                            a += 2
                    elif grammar_18_uni[a + 1] == 47532:  # "리"
                        if grammar_18_uni[a + 2] == 44256:  # 그리고
                            code_3rd.all_list[3][0] = 5
                            a += 2
                        elif grammar_18_uni[a + 2] == 54616:  # "하"
                            if grammar_18_uni[a + 3] == 50668:  # 그리하여
                                code_3rd.all_list[3][0] = 6
                                a += 3
            else:   # 공백이 아닌 경우
                continue

        a += 1


"""
    if code_3rd.data[a] == 0:
        print(0)

"""
# 테스트용
code_3rd.uni_set()
grammar_10()
grammar_11()

for i in range(code_3rd.count):
    if grammar_10_count[i] == 1:
        print(i)
    elif grammar_11_count[i] == 1:
        print(i)
    else:
        print("X")
