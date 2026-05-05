# -------------------------
# title: 
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: 
# AI2 InfinityLabs.
# ----------------------------

def linear_sort(s: str) -> str:
    m = ''
    ascii_n = 128
    ls = [0] * ascii_n
    for element in s:
        ls[ord(element)] += 1
    for i in range(ascii_n):
        while ls[i] != 0:
            m += chr(i)
            ls[i] -= 1
    return m


def main():
    cases = ['hello', 'hi mom', 'hello world my name is Daniel Merchav']
    results = ['ehllo', ' himmo', '      DMaaacdeeeehhiillllmmnnoorrsvwy']
    tests = zip(cases, results)
    for case, result in tests:
        print(case)
        assert linear_sort(case) == result, f'Test failed for case: {case}'


if __name__ == '__main__':
    main()
    print('Done.')
