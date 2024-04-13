def main():
    book_text = "" #holds book text
    book_path = "books/frankenstein.txt"

    with open(book_path) as f:
        book_text = f.read()

    print("Words in file:")
    print(get_word_count(book_text))
    
    print()

    print("Character Counts:")
    print(get_character_count(book_text))
    
    return

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