# Функция для определения четного числа
def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# Функция для определения максимального числа
def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Функция для определения минимального числа
def find_min(numbers):
    if not numbers:
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

# Сортировка чисел в порядке возрастания
def custom_sort(numbers):
    sorted_numbers = numbers.copy()
    for i in range(len(sorted_numbers)):
        for j in range(i + 1, len(sorted_numbers)):
            if sorted_numbers[i] > sorted_numbers[j]:
                sorted_numbers[i], sorted_numbers[j] = sorted_numbers[j], sorted_numbers[i]
    return sorted_numbers

# Чтение ввода от пользователя
input_str = input("Введите список чисел через запятую: ")
numbers = [int(num.strip()) for num in input_str.split(',')]

# Вызов функций
even_numbers = get_even_numbers(numbers)
max_num = find_max(numbers)
min_num = find_min(numbers)
sorted_numbers = custom_sort(numbers)

# Вывод результатов
print(f"Четные числа: {even_numbers}")
print(f"Максимальное число: {max_num}")
print(f"Минимальное число: {min_num}")
print(f"Отсортированный список: {sorted_numbers}")