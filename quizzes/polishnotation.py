# -------------------------
# title: Polish Notation.
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ------------------------------
# Author: Daniel Merchav.
# Reviewer: Alexander Volkovich.
# AI2 InfinityLabs.
# ------------------------------

def polish_notation(string):
    s = []
    ls = string.split()
    operators = ['+', '-', '*', '/']
    for element in reversed(ls):
        if element in operators:
            first = int(s.pop())
            second = int(s.pop())
            match element:
                case '*':
                    s.append(first * second)
                case '+':
                    s.append(first + second)
                case '-':
                    s.append(first - second)
                case '/':
                    s.append(first / second)
                case _:
                    raise ValueError
        else:
            s.append(element)
    return s[0]


def main():
    polish, results = ['+ * + 1 2 3 4', '+ 3 + 4 * 7 9', ' + 3 * -2 -3'], [13, 70, 9]
    for element in range(len(polish)):
        assert polish_notation(polish[element]) == results[element]


if __name__ == '__main__':
    main()
    print("Done.")
