def min_val_1(array):
    return min(array)


def min_val_2(array):
    res = array[0]
    for i in array:
        res = i if i < res else res
    return res


if __name__ == '__main__':
    arr = list(map(int, input("Введите массив: ").split()))
    print(min_val_1(arr))
    print(min_val_2(arr))
