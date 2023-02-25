# life=0
# while(life<=3):
#     if life==3:
#         break
#         life=life+1
#
#     a = int(input("Enter"))
#     if a>=20:
#         print("Greater")
#     elif a<=17:
#         print("lesser")
#     elif a==18:
#         print("osom")
num=18
life=4
while life<=4:
    life=life+1
    if life>4:
        print("lose")
        break
    else:
        x=int(input("Enter the intgere:"))
        if x==num:
            print("You won")
            break
        elif x<=num:
            print("lesser")
        elif x>=num:
            print("greater")
            continue


