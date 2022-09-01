import random
# Khai bao bien 
current_number = 0
current_player = random.randint(0,1)

if current_player == 0:
    # luot nguoi choi truoc
    print("Người thắng nên người chơi trước")
    while True:
        player_choice = input("Nhập vào giá trị (1,2 hoặc 3): ")
        danhsach = [1,2,3]
        count = 0
        while count in danhsach:
            if count == player_choice:
                print("giá trị hợp lệ")
            
            count = 0
        current_number += int(player_choice)
        if current_number >= 21:
            print("Người chơi đã thua")
            break
        print(current_number)

        # luot choi cua may

        computer_choice = random.randint(1,3)
        print("Máy chọn ", computer_choice)
        current_number += int(computer_choice)
        if current_number >= 21:
            print("Người chơi đã thắng")
            break
        print(current_number)
else:
    print("Máy thắng nên máy chơi trước")
    while True:
        # luot choi cua may

        computer_choice = random.randint(1,3)
        print("Máy chọn ", computer_choice)
        current_number += int(computer_choice)
        if current_number >= 21:
            print("Người chơi đã thắng")
            break
        print(current_number)

        # luot cua nguoi

        player_choice = input("Nhập vào giá trị (1,2 hoặc 3): ")
        danhsach = [1,2,3]
        count = 0
        while count in danhsach:
            if count == player_choice:
                print("giá trị hợp lệ")
            
            count = 0
        current_number += int(player_choice)
        if current_number >= 21:
            print("Người chơi đã thua")
            break
        print(current_number)