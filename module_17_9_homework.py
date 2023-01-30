def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = list(filter(lambda x: x < pivot, array))
        center = [i for i in array if i == pivot]
        greater = list(filter(lambda x: x > pivot, array))

    return quick_sort(less) + center + quick_sort(greater)


def binary_search_one(array, item):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high)
        guess = array[mid]
        if guess == item:
            return mid - 1
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return f'Ты ввел {item}, такого числа нет в списке'


def binary_search_two(array, item):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high)
        guess = array[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return f'Ты ввел {item}, такого числа нет в списке'


try:
    sequence_of_numbers = input("Введи числа через пробел: ").split()
    user_number = float(input('Введи число: '))
    num_list = list(map(float, sequence_of_numbers))
    print(num_list)
    print(quick_sort(num_list))
    print(binary_search_one(quick_sort(num_list), user_number))
    print(binary_search_two(quick_sort(num_list), user_number))
except ValueError:
    print("Вводите только числа!")
