# reviewer: anan.
def c_to_f(deg):
    return 9 / 5 * deg + 32


assert c_to_f(30) == 86
for temp in range(0, 51, 10):
    print(f'Degrees in C: {temp}. Degrees in F: {c_to_f(temp)}.')
