def sort_on(dictionary):
    return dictionary["count"]  # Changed from dictionary(["num"]) to dictionary["count"]

def sort_dict(input_dict):
    dict_list = []
    for k, v in input_dict.items():
        dict_list.append({"char": k, "count": v})  # Changed "num" to "count"
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    char_dict = {}
    for char in text:
        if char.lower() in char_dict:
            char_dict[char.lower()] +=1
        else:
            char_dict[char.lower()] = 1
    return(char_dict)