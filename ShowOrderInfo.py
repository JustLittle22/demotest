price = int(input("Nhập vào số tiền mua ($): "))

if price >= 150:
    print("Số tiền phải thanh toán: ", price - 50, "$")
elif price >= 100:
    print("Số tiền phải thanh toán: ", price - 25, "$")
elif price >= 75:
    print("Số tiền phải thanh toán: ", price - 15, "$")
else:
    print("Số tiền phải thanh toán: ", price, "$")