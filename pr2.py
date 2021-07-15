def f21(f):
    if f[2] == 'tcsh':
        if f[0] == 'bro':
            if f[1] == 'bison':
                if f[4] == 'zimpl':
                    return 0
                elif f[4] == 'alloy':
                    return 1
                elif f[4] == 'x10':
                    return 2
            elif f[1] == 'hy':
                if f[4] == 'zimpl':
                    return 3
                elif f[4] == 'alloy':
                    return 4
                elif f[4] == 'x10':
                    return 5
            elif f[1] == 'urweb':
                if f[4] == 'zimpl':
                    return 6
                elif f[4] == 'alloy':
                    return 7
                elif f[4] == 'x10':
                    return 8
        elif f[0] == 'metal':
            return 9
    elif f[2] == 'c':
        return 10


def f22(f):
    bf = bin(f)
    d = f & 0b10000000000000000000000000000000
    c = f & 0b01111111000000000000000000000000
    b = f & 0b00000000111111110000000000000000
    a = f & 0b00000000000000001111111111111111
    d = d >> 15
    b = b << 1
    c = c << 1
    return a | b | c | d




def f23(x):
    for i in range(len(x)):
        while None in x[i]:
            x[i].remove(None)
        for j in range(len(x[i])):
            if j == 0:
                x[i][j] = x[i][j].split(';')
            if j == 1:
                if x[i][j] == 'Не выполнено':
                    x[i][j] = 'N'
                if x[i][j] == 'Выполнено':
                    x[i][j] = 'Y'
            if j == 0:
                for k in range(len(x[i][j])):
                    x[i].append(x[i][j][k])
                for k in range(len(x[i][j])):
                    x[i][j].pop()
        x[i] = list(filter(None, x[i]))

    for i in range(len(x)):
        for j in range(len(x[i])):
            if j == 1:
                x[i][j] = x[i][j].replace('(', '')
                x[i][j] = x[i][j].replace(')', '')
                x[i][j] = x[i][j][0:10] + x[i][j][11:13]
            if j == 3:
                x[i][j] = x[i][j].replace('.', '-')
            if j == 2:
                x[i][j] = x[i][j].replace('[at]', '@')
    x = list(filter(None, x))

    for i in range(len(x)):
        date = x[i].pop(-1)
        x[i].insert(0, date)

    return x
