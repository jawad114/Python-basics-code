# class testing():
#     leaves = 10
#     pass
#
# shah = testing()
# khan = testing()
# shah.name = "jawad shah\n"
# khan.name = "\nSalman Khan\n"
# shah.rollno = 22222
# khan.rollno = 89939
# print(testing.leaves)
# # print(shah.name, shah.rollno , "\n", khan.rollno, khan.name)
# print(shah.__dict__)
# khan.leaves = 9
# print(testing.leaves)
# print(khan.__dict__)
class testing():
    leaves = 213
    pass
khan = testing()
shah = testing()
khan.name = "jawad shah"
khan.roll = "Student"
khan.sq = 389462
shah.name = "Jawad Shah"
shah.roll = "progammer"
print("\n",khan.name)
print("\n",khan.sq)
print("\n",khan.roll)
print(khan.__dict__)
testing.leaves = 38
print(testing.leaves)
print(khan.__dict__)
print(khan.leaves)
khan.leaves = 32
print(khan.leaves)
print(khan.__dict__)

