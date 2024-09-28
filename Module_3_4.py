def check_name(name_1, name_2):
    list_for_comparison = []
    count = 0
    for i in name_1.lower():
        count += 1
        if count < len(name_2):
            if i == name_2[count - 1].lower():
                list_for_comparison.append(i)
            else:
                count = 0
                continue
        else:
            if i == name_2[count - 1]:
                return True


def single_root_words(root_word, *other_words):
    same_words = []
    comparison = False
    for i in other_words:
        if len(root_word) < len(i):
            comparison = check_name(i, root_word)
            if comparison == True:
                same_words.append(i)
        else:
            comparison = check_name(root_word, i)
            if comparison == True:
                same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
