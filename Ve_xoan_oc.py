import turtle

khoang_cach = int(input("Nhập vào độ dài cần vẽ: "))
anh_screen = turtle.Screen()


pencil = turtle.Turtle()
pencil.speed(1)
tang_do_rong = 0.25
do_rong = 0.0
i = 0

while True:
    if turtle.distance(0,do_rong) > khoang_cach:
        break
    do_rong += tang_do_rong
    while i < 180:
        pencil.left(1)
        pencil.forward(do_rong)
        i += 1   
    i = 0  
turtle.done()