
def get_min_number(numbers):
    result = numbers[0]
    for i in numbers:
        if result > i:
            result = i
    return result
    
numbers = [9,8,4,25,41,12,32]
GTNN = get_min_number(numbers)
print("Giá trị nhỏ nhất là ", GTNN)