# def sq(a):
#     return a*a
#
# lis={1,2,4,77,89,5,7}
# number=list(map(sq, lis))
# number.remove(4)
# print(number)
# def great(num):
#     return num>5
# item = {1,3,4,6,7,8,9,0,66,4,33,336,676,43,}
# number = list(filter(great, item))
# print(number)
from functools import reduce
# item = {2,4,5,67,8}
#
# number = reduce(lambda x,y:x+y, item)
# print(number)
item=1
while item<=5:
    item=item+1
    num = reduce(lambda item:item*item, item)