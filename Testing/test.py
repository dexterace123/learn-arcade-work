for i in range(1,10):
    for j in range(10-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1, 0, -1):
        print(j,end=" ")
    print()
for i in range(1,9):
    for j in range(1, 2+i):
        print(" ",end=" ")
    for j in range(1, 10-i):
        print(j, end=" ")
    for j in range(8-i, 0, -1):
        print(j, end=" ")
    print()
