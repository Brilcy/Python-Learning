# 3. What a program to remove duplicate from list.
#    Example -
#    Input : [5, 1, 5, 17, 8, 1, 5]
#    Output : [5, 1, 17, 8]


def remove_duplicates(ip):
    # ip = [5, 1, 5, 17, 8, 1, 5]
    op = []
    d = {}
    for i in ip:
        if i not in d:
            d[i] = 1
            op.append(i)
    return print(op)


remove_duplicates([5, 1, 5, 17, 8, 1, 5])
