txt = "một với một là hai, hai thêm hai là bốn, bốn với một là năm, năm ngón tay thật đều"

def count_word(word, text):
    dictionary = {}
    text_list = text.split()
    word = word.lower()
    if word in text_list:
        for kitu in text_list:
            kitu = kitu.lower()
            if kitu not in dictionary:
                dictionary[kitu] = 1
            else:
                dictionary[kitu] += 1
        
        return f'{word} : {dictionary[word]}'
    else:
        return f"{word} : '0'"

word = input("Nhập từ cần tìm: ")
num_words = count_word(word, txt)
print(num_words)


