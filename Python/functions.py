n=0
def sums (a,b):
    """
    :param a:
    :param b:
    :return:
    """
    total=0
    print("a:",a)
    print("b:",b)

    total=a+b
    print("Total inside fun is ",total)
    return total

n=sums(5,7)
print("Total outside function:",n)



# Default Arguments
# n=0
# def sum (a,b=0):
#     total=0
#     print("a:",a)
#     print("b:",b)
#
#     total=a+b
#     print("Total inside fun",total)
#     return total
#
# n=sum(5)
# print("Total outside function:",n)


