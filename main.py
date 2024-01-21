from string import ascii_lowercase

def count_words(contents):
    return len(contents.split())
    
def read_text(path):
    with open(path) as f:
        return f.read()

def split_into_letters(text):
    dict_add = {}
    for letter in text:
        if not letter in dict_add and letter in ascii_lowercase:
            dict_add[letter] = 1
        if letter in ascii_lowercase:
            dict_add[letter] += 1
    return dict_add

def sorted_dict(dict_to_sort):
    sorted_list = []
    for key, value in dict_to_sort.items():
        sorted_list.append({'letter': key, 'amount': value})
    sorted_list.sort(reverse=True, key=lambda x: x["amount"])
    return sorted_list

def main():
    path = "books/frankenstein.txt"
    text_from_path = read_text(path)
    num_of_words = count_words(text_from_path)
    counted_letters = split_into_letters(text_from_path.lower())
    sorted_dict_to_list = sorted_dict(counted_letters)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words} words found in the document\n")
    for item in sorted_dict_to_list:
        print(f"The {item["letter"]} character was found {item["amount"]} times")
    print("--- End report ---")


main()