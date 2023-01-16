# 1. Write a program to print positive numbers from alist
#    Example -
#    Input : [5, 19, -10, 6, -7]
#    Output : 5, 19, 6


def positive_list(alist):
    # alist =[1,-5,-10,0,22,88,-3]
    for a in alist:
        if a >= 0:
            print(a)
    return 0


positive_list([1, -5, -10, 0, 22, 88, -3])
