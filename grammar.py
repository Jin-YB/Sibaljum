import code_3rd

grammar_10_uni = []
grammar_10_count = [0] * code_3rd.count
grammar_11_uni1 = []
grammar_11_count = [0] * code_3rd.count
grammar_18_uni = [0] * code_3rd.count
grammar_11_uni = []
grammar_12_uni = []


def grammar_10(a):

    for i in range(code_3rd.count):
        grammar_10_uni.append(((code_3rd.uni_data[i] - 44032) % 588) % 28)

    # 제 10항 모음 + '예' 50696 모음

        if grammar_10_uni[a] == 0:
            if 50726 >= code_3rd.uni_data[b] >= 50696:
                code_3rd.all_list[3][0] = 0
            else:
                code_3rd.all_list[3][0] = -1


def grammar_11(a):
    # 제 11항 모음(ㅑ,ㅘ,ㅜ,ㅝ) + '애' 50528 모음
    for i in range(code_3rd.count):
        grammar_11_uni.append(((code_3rd.uni_data[i] - 44032) % 588) % 28)

    if grammar_11_uni[a] == 0:
        for i in range(24):
            if code_3rd.uni_data[a] == (44088 + (588 * i)) or code_3rd.uni_data[a] == (44284 + (588 * i)) or \
                        code_3rd.uni_data[a] == (44396 + (588 * i)) or code_3rd.uni_data[a] == (44424 + (588 * i)):
                if 50555 >= code_3rd.uni_data[b] >= 50528:  # 애 ~ 앻
                    code_3rd.all_list[3][0] = 0
                else:
                    code_3rd.all_list[3][0] = -1
        a += 1


def grammar_12(a):
    for i in range(code_3rd.count):
        grammar_12_uni.append(code_3rd.uni_data[i])
        code_3rd.jong_uni.append(((code_3rd.uni_data[i] - 44032) % 588) % 28)  # 종성

    # all_list[3][0]: {0,~11}={이음줄,가,나,다,마,바,사,자,카,타,파,하}

    if 44032 <= grammar_12_uni[a] <= 44059:
        code_3rd.all_list[3][0] = 1

    elif 445208 <= grammar_12_uni[a] <= 45235:
        code_3rd.all_list[3][0] = 2

    elif 45796 <= grammar_12_uni[a] <= 45823:
        code_3rd.all_list[3][0] = 3

    elif 47560 <= grammar_12_uni[a] <= 47587:
        code_3rd.all_list[3][0] = 4

    elif 48148 <= grammar_12_uni[a] <= 48175:
        code_3rd.all_list[3][0] = 5

    elif 49324 <= grammar_12_uni[a] <= 49351:
        code_3rd.all_list[3][0] = 6

    elif 51088 <= grammar_12_uni[a] <= 51115:
        code_3rd.all_list[3][0] = 7

    elif 52852 <= grammar_12_uni[a] <= 52879:
        code_3rd.all_list[3][0] = 8

    elif 53440 <= grammar_12_uni[a] <= 53467:
        code_3rd.all_list[3][0] = 9

    elif 54028 <= grammar_12_uni[a] <= 54055:
        code_3rd.all_list[3][0] = 10

    elif 54616 <= grammar_12_uni[a] <= 54643:
        code_3rd.all_list[3][0] = 11

    else:
        code_3rd.all_list[3][0] = -1

    code_3rd.all_list[0][0] = -1
    code_3rd.all_list[0][1] = -1
    code_3rd.all_list[0][2] = code_3rd.jong_uni[a]


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
                        code_3rd.all_list[3][1] = 0
                        a += 2
                elif grammar_18_uni[a+1] == 47084:    # "러"
                    if grammar_18_uni[a+2] == 45208:   # 그러나
                        code_3rd.all_list[3][1] = 1
                        a += 2
                    elif grammar_18_uni[a+2] == 47732:   # 그러면
                        code_3rd.all_list[3][1] = 2
                        a += 2
                    elif grammar_18_uni[a+2] == 48064:   # "므"
                        if grammar_18_uni[a+3] == 47196:   # 그러므로
                            code_3rd.all_list[3][1] = 3
                            a += 3
                elif grammar_18_uni[a+1] == 47088:   # "런"
                    if grammar_18_uni[a+2] == 45936:   # 그런데
                        code_3rd.all_list[3][1] = 4
                        a += 2
                elif grammar_18_uni[a+1] == 47532:   # "리"
                    if grammar_18_uni[a+2] == 44256:   # 그리고
                        code_3rd.all_list[3][1] = 5
                        a += 2
                    elif grammar_18_uni[a+2] == 54616:   # "하"
                        if grammar_18_uni[a+3] == 50668:   # 그리하여
                            code_3rd.all_list[3][1] = 6
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

i = 0
while i < code_3rd.count:
    b = i + 1

    if code_3rd.count - 1 == i:
        if code_3rd.all_list[3][0] == 0:
            print(i)
        elif code_3rd.all_list[3][0] == -1:
            print("X")
        break
    grammar_10(i)
    if code_3rd.all_list[3][0] == 0:
        print(i)
    elif code_3rd.all_list[3][0] == -1:
        print("X")


    i += 1

"""grammar_11(i)
    if code_3rd.all_list[3][0] == 0:
        print(i)
    elif code_3rd.all_list[3][0] == -1:
        print("X")
    grammar_12(i)
    if code_3rd.all_list[3][0] == 0:
        print(i)
    elif code_3rd.all_list[3][0] == -1:
        print("X")"""
