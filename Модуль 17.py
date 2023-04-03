def binary_search(arr, low, high, x):
    # Проверка наличия элемента в списке
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


def sort_list(list_to_sort):
    # Функция сортировки списка
    return sorted(list_to_sort)


user_input = input("Введите последовательность чисел через пробел: ")
user_input_list = user_input.split()
try:
    user_input_list = [int(i) for i in user_input_list]
except ValueError:
    print("Ошибка: в последовательности присутствуют нечисловые значения.")
else:
    sorted_list = sort_list(user_input_list)
    search_value = input("Введите число: ")
    try:
        search_value = int(search_value)
    except ValueError:
        print("Ошибка: введено нечисловое значение.")
    else:
        index = binary_search(sorted_list, 0, len(sorted_list) - 1, search_value)
        if index == -1:
            print("Введенное число отсутствует в последовательности.")
        else:
            if index == 0:
                print(f"Введенное число меньше всех элементов списка.")
            elif index == len(sorted_list) - 1:
                print(f"Введенное число больше всех элементов списка.")
            else:
                print(f"Позиция элемента, меньшего введенного числа, равна {index}.")
                print(f"Значение элемента: {sorted_list[index]}.")
                print(f"Позиция следующего за ним элемента, большего или равного введенному числу, равна {index + 1}.")
                print(f"Значение элемента: {sorted_list[index + 1]}.")


Пользователь сначала вводит последовательность чисел через пробел, которую мы преобразуем в список и сортируем. Затем запрашивается у пользователя любое число, которое мы проверяем на соответствие условию. Если пользователь ввел нечисловое значение, программа выдает соответствующее сообщение об ошибке.

Далее мы используем алгоритм двоичного поиска, чтобы найти позицию элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу. Если введенное число не найдено в списке, программа выдает соответствующее сообщение. Если введенное число меньше всех элементов списка, программа также выдает соответствующее сообщение. Если введенное число больше всех элементов списка, программа также выдает соответствующее сообщение. В противном случае программа выдает позицию элемента,def binary_search(arr, low, high, x):
    # Проверка наличия элемента в списке
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


def sort_list(list_to_sort):
    # Функция сортировки списка
    return sorted(list_to_sort)


user_input = input("Введите последовательность чисел через пробел: ")
user_input_list = user_input.split()
try:
    user_input_list = [int(i) for i in user_input_list]
except ValueError:
    print("Ошибка: в последовательности присутствуют нечисловые значения.")
else:
    sorted_list = sort_list(user_input_list)
    search_value = input("Введите число: ")
    try:
        search_value = int(search_value)
    except ValueError:
        print("Ошибка: введено нечисловое значение.")
    else:
        index = binary_search(sorted_list, 0, len(sorted_list) - 1, search_value)
        if index == -1:
            print("Введенное число отсутствует в последовательности.")
        else:
            if index == 0:
                print(f"Введенное число меньше всех элементов списка.")
            elif index == len(sorted_list) - 1:
                print(f"Введенное число больше всех элементов списка.")
            else:
                print(f"Позиция элемента, меньшего введенного числа, равна {index}.")
                print(f"Значение элемента: {sorted_list[index]}.")
                print(f"Позиция следующего за ним элемента, большего или равного введенному числу, равна {index + 1}.")
                print(f"Значение элемента: {sorted_list[index + 1]}.")
