# reviewer: Ran.
def rotate_list(list1, n=1):
    rotate = n % len(list1)

    return list1[rotate:] + list1[:rotate]


list2 = [1, 2, 3, 4]

assert [2, 3, 4, 1] == rotate_list(list2)
print(rotate_list(list2))
