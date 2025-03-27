def count_words(book):
    words=[]
    words = book.split()
    num_word=len(words)
    return num_word

def count_char(book):
    let_count={}
    words = book.split()
    for word in words:
        low_word = word.lower()
        for letter in low_word:
            let_count[letter] = let_count.get(letter, 0)+1
    return let_count

def char_sort(let_count):
    def sort_on(temp):
        return temp["number"]
    letter_list = []
    for char in let_count:
        if char.isalpha():
            pass
        else:
            continue
        temp_dict = {}
        temp_dict["character"] = char
        temp_dict["number"] = let_count[char]
        letter_list.append(temp_dict)
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list
