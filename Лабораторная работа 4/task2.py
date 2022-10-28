def get_count_char(str_):
    dict_ = {}
    clear_ = "".join(str_.lower())
    for i in clear_:
        if i.isalpha():
            dict_[i] = dict_.get(i, 0) + 1
    return dict_


def proc(str_):
    str_ = {key: round(value / sum(str_.values()) * 100, 2) for key, value in str_.items()}
    return str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список 
    отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. 
    Приступим!!!!
"""
print(get_count_char(main_str))
print(proc(get_count_char(main_str)))
