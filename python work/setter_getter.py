# class student:
#     def __init__(self, fname, lname):
#         self.name=fname
#         self.roll=lname
#         def test(self):
#             return f"the name is {self.fname} and roll is {self.lname}"
# shah = student()
# print(shah.fname)
#
import time
from functools import lru_cache
@lru_cache(maxsize=0)
def harry(n):
    time.sleep(n)
    print("jawad shah")
    return n
if __name__ == '__main__':
    print("Executing.....")
    harry(3)
    print("done")
    harry(3)
    print("done again")

