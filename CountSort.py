count = [[0]* 100 for i in range(100)]
while b := input():
    b = eval(b)
    count[b[0]-1][b[1]-1] += 1
for i in range(100):
    for j in range(100):
        while count[i][j] != 0:
            print(i + 1, j + 1, sep = ", ")
            count[i][j] -= 1