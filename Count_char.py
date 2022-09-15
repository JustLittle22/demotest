def count_char(txt):
    count = 0
    for char in txt:
        count += 1
    return count

txt = input("Enter your string: ")
print("Length string: ", count_char(txt))