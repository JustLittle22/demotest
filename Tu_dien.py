

dictionary = {
    'country':'đất nước',
    'happy':'vui vẻ',
    'dog':'con chó'
}

def translate(dictionary, word):
    if word in dictionary:
        print(word, ':', dictionary[word])
    else:
        print(word, 'does not exist')
       
input_word = input("Nhập từ cần tìm: ")
result = translate(dictionary, input_word)
print(result)

        