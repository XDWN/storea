lis = [1, 4, 7, 5, 8, 2, 1, 3, 4, 5, 9, 7, 6, 1, 10]
def list(a):
    from collections import Counter
    res = Counter(a)
    print(res)
list(lis)