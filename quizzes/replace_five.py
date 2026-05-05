def change_five(number):
    sm, sign = 0, 1
    ls = list(str(number))
    if number < 0:
        ls[:] = ls[1:]
        sign = -1
        for i in range(len(ls)):
            if ls[i] > '5':
                ls[i] = '5'
                break
    else:
        for i in range(len(ls)):
            if ls[i] < '5':
                ls[i] = '5'
                break
    ls = ls
    for i in range(len(ls)):
        sm += float(ls.pop()) * 10 ** i
    return sign * sm


print(change_five(6546))
