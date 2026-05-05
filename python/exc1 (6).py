# reviewer: Ran.
def intersect_list(list1, list2):
    return list(set(list1).intersection(list2))


ls1 = [1, 4, 6, 65, 2, 100]
ls2 = [1, 5, 2, 65, 7, 6, 4]

assert sorted(intersect_list(ls1, ls2)) == [1, 2, 4, 6, 65]
print(f'ls1: {ls1}.\nls2: {ls2}.\nThe intersect: {intersect_list(ls1, ls2)}')
"""bit operations"""
