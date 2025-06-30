def count_words(text):
    words_list  = text.split()
    num_words = len(words_list)
    return num_words


def count_chars(text):
    cha_dict = {}
    for cha in text.lower():
        if cha in cha_dict:
            cha_dict[cha] += 1
        else:
            cha_dict[cha] = 1
    return cha_dict


def sort_dict_on(items):
    return items["num"]


def report_chars(text):
    word_count = count_words(text)
    cha_dict = count_chars(text)
    dict_list = []
    for key, value in cha_dict.items():
        dict_list.append({"name": key, "num": value})

    dict_list.sort(reverse=True, key=sort_dict_on)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for pair in dict_list:
        if pair["name"].isalpha():
            print(f"{pair["name"]}: {str(pair["num"])}")
    print("============= END ===============")