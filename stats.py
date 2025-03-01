def get_num_words(text_string):
    word_list = text_string.split()
    num = 0
    for word in word_list:
        num += 1
    return str(num)

def get_num_char(text_string):
    char_dict = {}
    word_list = text_string.split()
    for word in word_list:
        temp_char_list = list(word.lower())
        for c in temp_char_list:
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1

    return char_dict

def sort_on(char_dict):
    return char_dict["count"]

def sorted_dicts_report(char_dict):

    dict_list = []
    for key in char_dict:
        if key.isalpha():
            temp_dict = {"char": key, "count": char_dict[key]}
            dict_list.append(temp_dict)

    dict_list.sort(reverse=True, key=sort_on)
    
    return dict_list