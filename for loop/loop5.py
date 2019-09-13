a = int(input("a? "))
for i in range(a):
    ws = ' ' * (a - i - 1)
    st = '*' * i
    print(ws + st + '*' + st + ws)