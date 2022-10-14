list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
maks = max(list_numbers)
point = list_numbers.index(maks)
list_numbers[point] = list_numbers[-1]
list_numbers[-1] = maks
print(list_numbers)
