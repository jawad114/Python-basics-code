# # def testting(a):
# # # # cont = ("jawad", "shah", "Zaid", "Saad", "khan")
# # # cont = {1,2,3,4,5,6,6,7,7,8,89,0}
# # # for item in cont:
# # #     if cont>=6:
# # #         print(cont)
# # a = int(input("Enter the integer:"))
# # while 1:
# #  0   if a<100:
# #         continue
# #     else:
# #         print("Sorry")
# # testing(9)
#  """
#   nshcHEDIOEJOWEKOKASDJACMjdomd;lqKDOkdkqFK,MOJ,.JAWTYEFJH
#     print(testting.__doc__) """
#
# #     # print(a)
# # print(testting.__doc__ )
# #
# # # testting(int(input("Enter the intgre")))
a=input()
b=input()
try:
 print(int(a)+int(b))
except Exception as e:
 print(e)



 print("Am The last line if yiur program")
 from flask import Flask

 app = Flask(__name__)


 @app.route("/")
 def hello():
  return "Hello, World!"