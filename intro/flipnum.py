# reviewer: anan.
def flip_num(num):
    string = str(num)

    if string[0] == "-":
        return type(num)("-" + string[:0:-1])
    return type(num)(string[::-1])


assert flip_num(123) == 321
for number in range(-123, 32, 20):
    print(f'Number: {number}. flipped: {flip_num(number)}')
