from random import randint


def input_handler():
    """Обработка ввода"""
    arr = []
    temp = int(input("Select:\nAuto - 1\tManual - 2\n"))
    if temp == 1:
        for i in range(10):
            arr.append(randint(0, 10))
        print(arr)
    elif temp == 2:
        while True:
            try:
                arr = list(map(int, input("input your values: ").split()))
                if arr:
                    break
                else:
                    print("INPUT ERROR")
            except ValueError:
                print("ONLY INTEGER")
    return arr


def update_list():
    """Алгоритм с использованием встроенных функций"""

    arr = input_handler()

    max_ind = [arr.index(max(arr)), len(arr) - arr[::-1].index(max(arr)) - 1]  # Поиск индексов первого и последнего
    min_ind = [arr.index(min(arr)), len(arr) - arr[::-1].index(min(arr)) - 1]  # вхождения максимума и минимума

    if abs(min_ind[0] - max_ind[1]) > abs(max_ind[0] - min_ind[1]):  # Поиск наиболее длинного отрезка между
        field = [min_ind[0], max_ind[1]]                             # максимальным и минимальным значением
    else:
        field = [max_ind[0], min_ind[1]]
    field.sort()

    res = arr[:field[0] + 1]  # Запись подходящих значений в новый массив
    for i in range(field[0] + 1, field[1]):
        if arr[i] % 2 != 0:
            res.append(arr[i])
    res += arr[field[1]:]

    return res


def update_list_my():
    """Алгоритм без использования встроенных функций"""

    arr = input_handler()
    lmax = lmin = rmax = rmin = 0

    for i in range(len(arr)):  # Поиск индексов первого и последнего
        if arr[i] > arr[lmax]:  # вхождения максимума и минимума
            lmax = i
        if arr[i] < arr[lmin]:
            lmin = i
        if arr[i] >= arr[rmax]:
            rmax = i
        if arr[i] <= arr[rmin]:
            rmin = i

    temp_field_first = [lmax, rmin] if lmax < rmin else [rmin, lmax]  # Поиск наиболее длинного отрезка между
    temp_field_sec = [lmin, rmax] if lmin < rmax else [rmax, lmin]  # максимальным и минимальным значением

    if temp_field_first[1] - temp_field_first[0] > temp_field_sec[1] - temp_field_sec[0]:
        field = temp_field_first
    else:
        field = temp_field_sec

    res = arr[:field[0] + 1]   # Запись подходящих значений в новый массив
    for i in range(field[0] + 1, field[1]):
        if arr[i] % 2 != 0:
            res.append(arr[i])
    res += arr[field[1]:]

    return res


if __name__ == '__main__':
    print(update_list_my())
