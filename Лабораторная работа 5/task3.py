import random


def get_unique_list_numbers() -> list[int]:
    list_num = []
    a = 0
    while a != 15:
        g = random.randint(-10, 10)
        if g not in list_num:
            list_num.append(g)
            a += 1
    return list_num


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
