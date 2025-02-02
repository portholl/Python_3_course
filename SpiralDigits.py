a = eval(input())
st = "0123456789"
ansv = [[-1]  * a[0] for i in range(a[1])]
row = 0
col = 0
direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
current_direction = 0
for i in range(a[1] * a[0]):
    ansv[row][col] = st[i % 10]
    next_row = row + direction[current_direction][0]
    next_col = col + direction[current_direction][1]
    if 0 <= next_row  < a[1] and 0 <= next_col  < a[0] and ansv[next_row % a[1]][next_col % a[0]] == -1:
        row = next_row % a[1]
        col = next_col % a[0]
    else:
       current_direction = (current_direction + 1) % 4
       next_row = row + direction[current_direction][0]
       next_col = col + direction[current_direction][1]
       row = next_row % a[1]
       col = next_col % a[0]
for i in ansv:
    print(*i)