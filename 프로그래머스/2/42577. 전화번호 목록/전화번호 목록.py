def solution(phone_book):
    my_hash = {}
    word=""
    for num in phone_book:
        my_hash[num] = True
    for num in my_hash:
        my_hash[num] = False
        for char in num[:-1]:
            word +=char
            if word in my_hash:
                return False
        word = ""
        my_hash[num] = True
    return True