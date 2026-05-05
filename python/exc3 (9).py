# reviewer: Ran.
def print_list_even(ls):
    start = 1

    while ls:
        for elem in ls[start::2]:
            print(elem)
            ls.remove(elem)
        start = (len(ls) - start) % 2

    return


ls1 = [1, 2, 3, 4, 5]

print_list_even(ls1)
