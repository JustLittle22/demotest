Can_nang = int(input("Nhập vào cân nặng (kg) của bạn: "))
Chieu_cao = int(input("Nhập vào chiều cao (cm) của bạn: "))
Chuyen_chieu_cao = Chieu_cao/100
Chi_so_BMI = Can_nang / (Chuyen_chieu_cao**2)

if Chi_so_BMI < 16:
    print("Gầy cấp độ III")
elif Chi_so_BMI >= 16 and Chi_so_BMI < 17:
    print("Gầy cấp độ II")
elif Chi_so_BMI >= 17 and Chi_so_BMI < 18.5:
    print("Gầy cấp độ I")
elif Chi_so_BMI >= 18.5 and Chi_so_BMI < 25:
    print("Bình thường")
elif Chi_so_BMI >= 25 and Chi_so_BMI < 30:
    print("Thừa cân")
elif Chi_so_BMI >= 30 and Chi_so_BMI < 35:
    print("Béo phì cấp độ I")
elif Chi_so_BMI >= 35 and Chi_so_BMI < 40:
    print("Béo phì cấp độ II")
else:
    print("Béo phì cấp độ III")