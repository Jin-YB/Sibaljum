import code_3rd


code_3rd.uni_set()
# 12항 약자

for i in range(code_3rd.count):
    grammar_11_uni1.append(((code_3rd.uni_data[i] - 44032) % 588) % 28)

a = 0
while a < code_3rd.count:
    b = a + 1
    if code_3rd.count - 1 == a:
        break

    if grammar_11_uni1[a] == 0:
        for i in range(24):
            if code_3rd.uni_data[a] == (44088+(588*i)) or code_3rd.uni_data[a] == (44284+(588*i)) or code_3rd.uni_data[a] == (44396+(588*i)) or code_3rd.uni_data[a] == (44424+(588*i)):
                if 50555 >= code_3rd.uni_data[b] >= 50528:  # 애 ~ 앻
                    grammar_11_count[a] = 1
                else:
                    grammar_11_count[a] = 0
    a += 1




# 테스트용
for i in range(code_3rd.count):
    if grammar_11_count[i] == 1:
        print(i)
    else:
        print("X")