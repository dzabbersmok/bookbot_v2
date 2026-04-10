def sort_on(items):
    return items["num"]

def char_sort(char_count):
    char_list = []
    for char in char_count:
        char_list.append({"char": char, "num": char_count[char]})

    char_list.sort(reverse=True, key=sort_on)
    return char_list

def word_count(text):
    return len(text.split())

def char_counter(text):
    char_count = {}
    for char in text:
        lc_char = char.lower()
        if lc_char in char_count:
            char_count[lc_char] += 1
        else:
            char_count[lc_char] = 1
    
    return char_count