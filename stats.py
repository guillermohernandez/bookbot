def count_words(file_content):
    num_words = len(file_content.split())
    return num_words

char_dict = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
    ".": 0,
    " ": 0
}
def count_chars(file_content):
    for char in file_content:
        lowercase_char = char.lower()
        if lowercase_char in char_dict:
            char_dict[lowercase_char] += 1
    return char_dict

def sort_on(items):
    return items["num"]


def sorted_dict(char_dict):
    char_list = []
    for key, value in char_dict.items():
        if key.isalpha():
            small_dict = {"char": key,"num": value,}
            char_list.append(small_dict)
    char_list.sort(reverse=True, key=sort_on)        
    return char_list      
