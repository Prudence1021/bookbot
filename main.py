def main():
    book_string = book_to_string(book_path)
    words = book_string.split()
    count = letter_count(book_string)
    sorted_dict = dict_to_list_dict(count)
    generate_report(sorted_dict)
    



def book_to_string(path):
    with open(path) as f:
        frankenstein = f.read()
    return frankenstein


def letter_count(string):
    count_dic = {}
    lower_string = string.lower()
    letter_list = list(lower_string)
    for letter in letter_list:
        if letter not in count_dic:
            count_dic[letter] = 1
        else:
            count_dic[letter] += 1
    return count_dic

def dict_to_list_dict(diction):
    list_dict = []
    for key in diction:
        new_dict = {}
        new_dict[key] = diction[key]
        if key.isalpha():
            list_dict.append(new_dict)
    list_dict.sort(reverse = True, key=sort_on)
    return list_dict

def sort_on(dicti):
    for key in dicti:
        return dicti[key]



def generate_report(dict_list):
    print(f"--- Begin report of {book_path} ---")
    for i in dict_list:
        new_dict = i
        for key in new_dict:
            print(f"The '{key}' character was found {new_dict[key]} times")
    print("--- End report ---")


book_path = "books/frankenstein.txt"
main()
