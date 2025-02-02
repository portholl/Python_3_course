def max_integer(text):
    integers = []
    for i in text:
        if i[0] == "-" and  i[1:].isdecimal():
            integers.append(int(i))
        elif i.isdecimal():
            integers.append(int(i))

    if integers:
        return max(integers)
    else: return 0

text = []
while a:= input():
    text += a.split()
print(max_integer(text))