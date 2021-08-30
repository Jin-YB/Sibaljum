import code_3rd


grammar_10_uni = []
grammar_11_uni = []
grammar_12_uni = []
grammar_12_2_uni1 = []
grammar_12_2_uni2 = []
grammar_12_2_uni3 = []
grammar_18_uni = []


def grammar_10(a):

    for i in range(code_3rd.count):
        grammar_10_uni.append(((code_3rd.uni_data[i] - 44032) % 588) % 28)

    # 제 10항 모음 + '예' 50696 모음

    if grammar_10_uni[a] == 0:
        if 50726 >= code_3rd.uni_data[a+1] >= 50696:
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
                if 50555 >= code_3rd.uni_data[a+1] >= 50528:  # 애 ~ 앻
                    code_3rd.all_list[3][0] = 0
                else:
                    code_3rd.all_list[3][0] = -1
        a += 1


def grammar_12(a):
    for i in range(code_3rd.count):
        grammar_12_uni.append(code_3rd.uni_data[i])
        code_3rd.jong_uni.append(((code_3rd.uni_data[i] - 44032) % 588) % 28)  # 종성

    # all_list[3][0]: {0~11}={이음줄,가,나,다,마,바,사,자,카,타,파,하}

    if 44032 <= grammar_12_uni[a] <= 44059:
        code_3rd.all_list[3][0] = 1
        code_3rd.all_list[0][2] = code_3rd.jong_uni[a]

    elif 445208 <= grammar_12_uni[a] <= 45235:
        code_3rd.all_list[3][0] = 2
        code_3rd.all_list[0][2] = code_3rd.jong_uni[a]

    elif 45796 <= grammar_12_uni[a] <= 45823:
        code_3rd.all_list[3][0] = 3
        code_3rd.all_list[0][2] = code_3rd.jong_uni[a]

    elif 47560 <= grammar_12_uni[a] <= 47587:
        code_3rd.all_list[3][0] = 4
        code_3rd.all_list[0][2] = code_3rd.jong_uni[a]

    elif 48148 <= grammar_12_uni[a] <= 48175:
        code_3rd.all_list[3][0] = 5
        code_3rd.all_list[0][2] = code_3rd.jong_uni[a]

    elif 49324 <= grammar_12_uni[a] <= 49351:
        code_3rd.all_list[3][0] = 6
        code_3rd.all_list[0][2] = code_3rd.jong_uni[a]

    elif 51088 <= grammar_12_uni[a] <= 51115:
        code_3rd.all_list[3][0] = 7
        code_3rd.all_list[0][2] = code_3rd.jong_uni[a]

    elif 52852 <= grammar_12_uni[a] <= 52879:
        code_3rd.all_list[3][0] = 8
        code_3rd.all_list[0][2] = code_3rd.jong_uni[a]

    elif 53440 <= grammar_12_uni[a] <= 53467:
        code_3rd.all_list[3][0] = 9
        code_3rd.all_list[0][2] = code_3rd.jong_uni[a]

    elif 54028 <= grammar_12_uni[a] <= 54055:
        code_3rd.all_list[3][0] = 10
        code_3rd.all_list[0][2] = code_3rd.jong_uni[a]

    elif 54616 <= grammar_12_uni[a] <= 54643:
        code_3rd.all_list[3][0] = 11
        code_3rd.all_list[0][2] = code_3rd.jong_uni[a]


def grammar_12_2(a):
    grammar_12_2_uni1.append((code_3rd.uni_data[a] - 44032) // 588)  # 초성
    grammar_12_2_uni2.append(((code_3rd.uni_data[a] - 44032) % 588) // 28)  # 중성
    grammar_12_2_uni3.append(((code_3rd.uni_data[a] - 44032) % 588) % 28)  # 종성

    # 588

    if grammar_12_2_uni2 == 4:
        if grammar_12_2_uni3 == 2:
            code_3rd.all_list[3][0] = 12  # 억
            code_3rd.all_list[0][0] = grammar_12_2_uni1
            code_3rd.all_list[0][1] = -1
            code_3rd.all_list[0][2] = -1
        elif grammar_12_2_uni3 == 4:
            code_3rd.all_list[3][0] = 13  # 언
            code_3rd.all_list[0][0] = grammar_12_2_uni1
            code_3rd.all_list[0][1] = -1
            code_3rd.all_list[0][2] = -1
        elif grammar_12_2_uni3 == 8:
            code_3rd.all_list[3][0] = 14  # 얼
            code_3rd.all_list[0][0] = grammar_12_2_uni1
            code_3rd.all_list[0][1] = -1
            code_3rd.all_list[0][2] = -1
    elif grammar_12_2_uni2 == 6:
        if grammar_12_2_uni3 == 4:
            code_3rd.all_list[3][0] = 15  # 연
            code_3rd.all_list[0][0] = grammar_12_2_uni1
            code_3rd.all_list[0][1] = -1
            code_3rd.all_list[0][2] = -1
        elif grammar_12_2_uni3 == 8:
            code_3rd.all_list[3][0] = 16  # 열
            code_3rd.all_list[0][0] = grammar_12_2_uni1
            code_3rd.all_list[0][1] = -1
            code_3rd.all_list[0][2] = -1
        elif grammar_12_2_uni3 == 21:
            code_3rd.all_list[3][0] = 17  # 영
            code_3rd.all_list[0][0] = grammar_12_2_uni1
            code_3rd.all_list[0][1] = -1
            code_3rd.all_list[0][2] = -1
    elif grammar_12_2_uni2 == 8:
        if grammar_12_2_uni3 == 2:
            code_3rd.all_list[3][0] = 18  # 옥
            code_3rd.all_list[0][0] = grammar_12_2_uni1
            code_3rd.all_list[0][1] = -1
            code_3rd.all_list[0][2] = -1
        elif grammar_12_2_uni3 == 4:
            code_3rd.all_list[3][0] = 19  # 온
            code_3rd.all_list[0][0] = grammar_12_2_uni1
            code_3rd.all_list[0][1] = -1
            code_3rd.all_list[0][2] = -1
        elif grammar_12_2_uni3 == 21:
            code_3rd.all_list[3][0] = 20  # 옹
            code_3rd.all_list[0][0] = grammar_12_2_uni1
            code_3rd.all_list[0][1] = -1
            code_3rd.all_list[0][2] = -1
    elif grammar_12_2_uni2 == 13:
        if grammar_12_2_uni3 == 4:
            code_3rd.all_list[3][0] = 21  # 운
            code_3rd.all_list[0][0] = grammar_12_2_uni1
            code_3rd.all_list[0][1] = -1
            code_3rd.all_list[0][2] = -1
        elif grammar_12_2_uni3 == 8:
            code_3rd.all_list[3][0] = 22  # 울
            code_3rd.all_list[0][0] = grammar_12_2_uni1
            code_3rd.all_list[0][1] = -1
            code_3rd.all_list[0][2] = -1
    elif grammar_12_2_uni2 == 18:
        if grammar_12_2_uni3 == 4:
            code_3rd.all_list[3][0] = 23  # 은
            code_3rd.all_list[0][0] = grammar_12_2_uni1
            code_3rd.all_list[0][1] = -1
            code_3rd.all_list[0][2] = -1
        elif grammar_12_2_uni3 == 8:
            code_3rd.all_list[3][0] = 24  # 을
            code_3rd.all_list[0][0] = grammar_12_2_uni1
            code_3rd.all_list[0][1] = -1
            code_3rd.all_list[0][2] = -1
    elif grammar_12_2_uni2 == 20:
        if grammar_12_2_uni3 == 4:
            code_3rd.all_list[3][0] = 25   # 인
            code_3rd.all_list[0][0] = grammar_12_2_uni1
            code_3rd.all_list[0][1] = -1
            code_3rd.all_list[0][2] = -1
    else:
        code_3rd.all_list[3][0] = -1

    if grammar_12_2_uni1 == 0:
        if grammar_12_2_uni2 == 4:
            if grammar_12_2_uni3 == 9:
                code_3rd.all_list[3][0] = 26  # 것
                code_3rd.all_list[0][0] = -1
                code_3rd.all_list[0][1] = -1
                code_3rd.all_list[0][2] = -1


# all_list[3][0]={12~26}{억,언,얼,언,열,영,옥,온,옹,운,울,은,을,인,것}


""" 시작 글자 -> 그 """   # 앞자리 비었을때로 예외처리, all_list로 순서 정하기


def grammar_18(a):
    for j in range(code_3rd.count):
        grammar_18_uni.append(code_3rd.uni_data[j])
    if a == 0 or grammar_18_uni[a-1] == 32:   # 처음시작(빈공간 당연히 x)
        if grammar_18_uni[a] == 44536:   # "그"
            if grammar_18_uni[a+1] == 47000:    # "래"
                if grammar_18_uni[a+2] == 49436:    # 그래서
                    code_3rd.all_list[3][1] = 0

            elif grammar_18_uni[a+1] == 47084:    # "러"
                if grammar_18_uni[a+2] == 45208:   # 그러나
                    code_3rd.all_list[3][1] = 1

                elif grammar_18_uni[a+2] == 47732:   # 그러면
                    code_3rd.all_list[3][1] = 2

                elif grammar_18_uni[a+2] == 48064:   # "므"
                    if grammar_18_uni[a+3] == 47196:   # 그러므로
                        code_3rd.all_list[3][1] = 3

            elif grammar_18_uni[a+1] == 47088:   # "런"
                if grammar_18_uni[a+2] == 45936:   # 그런데
                    code_3rd.all_list[3][1] = 4

            elif grammar_18_uni[a+1] == 47532:   # "리"
                if grammar_18_uni[a+2] == 44256:   # 그리고
                    code_3rd.all_list[3][1] = 5

                elif grammar_18_uni[a+2] == 54616:   # "하"
                    if grammar_18_uni[a+3] == 50668:   # 그리하여
                        code_3rd.all_list[3][1] = 6




"""
    if code_3rd.data[a] == 0:
        print(0)

"""
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
