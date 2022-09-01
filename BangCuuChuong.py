number = input("Bảng cửu chương mấy? ")
print("Bảng cửu chương ", number)
for val in range(1,11):
    print(val, "*", number, "=", int(val)*int(number))