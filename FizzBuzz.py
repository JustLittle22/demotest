number1 = input("Nhập vào số thứ nhất: ")
number2 = input("Nhập vào số thứ hai: ")

if int(number1) >= int(number2):
    print("Số thứ hai phải lớn hơn số thứ nhất")
    number1 = input("Nhập vào số thứ nhất: ")
    number2 = input("Nhập vào số thứ hai: ")

    
for cnumber in range(int(number1), int(number2)):
    if cnumber % 3 == 0 and cnumber % 5 == 0:
        print("Fizzbuzz")
    elif  cnumber % 3 == 0:
        print("Fizz")
    elif cnumber % 5 == 0:
        print("Buzz")
    else:
        print(cnumber)