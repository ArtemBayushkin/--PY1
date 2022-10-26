import random


def get_unique_list_numbers(start=-10, stop=10, count=15) -> list[int]:
    list_num = []
    while len(list_num) != count:
        number = random.randint(start, stop)
        if number not in list_num:
            list_num.append(number)
    return list_num


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
