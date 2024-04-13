def main():
    book_text = "" #holds book text
    book_path = "books/frankenstein.txt"
    char_dic = {}
    char_lst = []
    char_lst_dic = {}

    with open(book_path) as f:
        book_text = f.read()

    print("--- Begin report of books/frankenstein.txt")
    print(get_word_count(book_text))
    
    print()

    char_dic = get_character_count(book_text)
    for char in char_dic:
        char_lst_dic = {"character": char, "count": char_dic[char]}
        if char.isalpha():
            char_lst.append(char_lst_dic)
    char_lst.sort(key=sort_on, reverse=True)
    for item in char_lst:
        print(f"The {item['character']} character was found {item['count']} times")
        
    print("--- End report ---")
    
    return

def sort_on(dict):
    # print(dict)
    return dict["count"]

def get_word_count(str_to_count):
    return len(str_to_count.split())

def get_character_count(str_to_count):
    character_dic = {}
    character_lst = []

    character_lst = list(str_to_count)
    for char in character_lst:
        char = char.lower()
        if char in character_dic:
            character_dic[char] += 1
        else:
            character_dic[char] = 1
    #print(character_dic)
    return character_dic

main()