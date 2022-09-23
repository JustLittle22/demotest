# Hàm in ra thông tin các option cần lựa chọn
def print_option():
    print('******************************')
    print("1. Thêm mới sản phẩm")
    print("2. Cập nhật lại sản phẩm")
    print("3. Xóa sản phẩm")
    print("4. Thoát khỏi danh sách sản phẩm")
    print('******************************')

# Hàm check xem sản phẩm có chưa?
def check_product_exist(prod_id,dict_product):
    if prod_id in dict_product.get('prod_id'):
        return True
        
    else:
        return False

# Hàm hiển thị sản phẩm được chọn
def show_product(product_id, dict_product):
    for value in dict_product.values():
        print(value[product_id])

# Thêm sản phẩm
def add_product(product_id, dict_product):
    name = input("Tên sản phẩm mới: ")
    for key in dict_product.values():
        key[product_id] = name
        print(dict_product['prod_id'])    
# Hàm Thêm mới sản phẩm
def add_new_product(dict_product):
    product_id = input("Nhập id sản phẩm: ")
    # Kiểm tra xem sản phẩm có chưa?
    check_product_exist(product_id, dict_product)
    
    # Có thì hiển thị sản phẩm
    if check_product_exist(product_id, dict_product) == True:
        show_product(product_id, dict_product)
        
    # Chưa có thì thêm mới sản phẩm
    else:
        add_product(product_id, dict_product)
    
    
# Hàm cập nhật danh sách sản phẩm
def update_product(dict_product):
    # In ra danh sách sản phẩm
    print(dict_product)
    product_id = input("Nhập id sản phẩm: ")
    # Kiểm tra sản phẩm có chưa?
    if check_product_exist(product_id, dict_product) == True:
    # Có thì hiển thị sản phẩm và cập nhật lại sản phẩm
        show_product(product_id, dict_product)
        add_product(product_id, dict_product)
    # Chưa có thì thêm mới sản phẩm
    else:
        add_product(product_id, dict_product)
    
# Hàm xóa sản phẩm
def remove_product(dict_product):
    product_id = input("Nhập id sản phẩm: ")
    # Kiểm tra sản phẩm có chưa?
    if check_product_exist(product_id, dict_product) == True:
    # Có thì hiển thị danh sách sản phẩm và xóa sản phẩm
        for value in dict_product.values():
            del value[product_id]
            print(dict_product)
    # Chưa có thì thông báo chưa có sản phẩm này
    else:
        print(product_id, "không tồn tại!")
    

dict_product = {'prod_id': {'0001' : 'Sữa', '0002' : 'Bánh', '0003' : 'Chuối'}}
while True:
    dict_product = dict_product
    print_option()
    option = int(input("Chọn option: "))
    
    if option == 1:
        add_new_product(dict_product)
        
    elif option == 2:
        update_product(dict_product)
        
    elif option == 3:
        remove_product(dict_product)
        
    elif option == 4:
        break
    else:
        print("Invalid")

print(dict_product['prod_id'])