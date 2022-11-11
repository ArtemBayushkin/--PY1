import random


def get_unique_list_numbers(start=-10, stop=10, count=15) -> list[int]:
    list_ = list(range(start, stop))
    random.shuffle(list_)
    list_ = list_[:count]
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
