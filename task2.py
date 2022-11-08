def get_count_char(str_):
    dict_ = {}
    str_ = str_.lower()
    for char in str_:
        if char.isalpha():
            if char in dict_.keys():
                dict_[char] += 1
            else:
                dict_[char] = 1
    return dict_


def get_count_char(str_):
    dict_ = {}
    str_ = str_.lower()
    for char in str_:
        if char.isalpha():
            dict_[char] = dict_.get(char, 0) + 1
    return dict_


def get_count_char(str_):
    str_ = str_.lower()
    dict_elem = {}
    for elem in str_:
        if elem.isalpha() and not dict_elem.get(elem):
            dict_elem[elem] = str_.count(elem)
    return dict_elem


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))