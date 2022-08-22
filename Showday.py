from ast import Num


Number = int(input("Nhập vào một số (từ 1 đến 7): "))

if Number == 1:
    print("Monday")
elif Number == 2:
    print("Tuesday")
elif Number == 3:
    print("Wednesday")
elif Number == 4:
    print("Thursday")
elif Number == 5:
    print("Friday")
elif Number == 6:
    print("Saturday")
else:
    print("Sunday")