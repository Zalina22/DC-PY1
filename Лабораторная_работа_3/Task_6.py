list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение

max_index = 0
max_namber = list_numbers[max_index]

for i, num in enumerate(list_numbers):
    max_number = list_numbers[max_index]
    if num > max_number:
        max_index = i
        max_namber = list_numbers[max_index]
list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index]
print(list_numbers)