list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_number = list_numbers [0]
for numbers in list_numbers:
    if numbers > max_number:
        max_number = numbers

print(max_number)
print(list_numbers)

list_numbers[9], list_numbers[-1] = list_numbers[-1], list_numbers[9]

# пробовала сделать max_number, list_numbers[-1] = list_numbers[-1], max_number  о максимальное значение не меняется. не понимаю почему
print(list_numbers)
