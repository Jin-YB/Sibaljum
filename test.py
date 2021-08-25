array = [[0 for col in range(11)] for row in range(10)]
array[3][1] = 1 
for i in array :
    for j in i:
        print(j,end=" ")
    print()